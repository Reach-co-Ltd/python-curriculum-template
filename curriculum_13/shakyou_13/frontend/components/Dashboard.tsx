"use client";
import { useState, useEffect } from "react";
import type { DashboardRow, DashboardTask } from "@/lib/api";
import { fetchDashboard } from "@/lib/api";

const toLocalISO = (dt: Date): string => {
  const y = dt.getFullYear();
  const m = String(dt.getMonth() + 1).padStart(2, "0");
  const d = String(dt.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
};
const today = () => toLocalISO(new Date());
const addDays = (d: string, n: number) => {
  const dt = new Date(d + "T00:00:00");
  dt.setDate(dt.getDate() + n);
  return toLocalISO(dt);
};
const fmtDate = (d: string) => {
  const dt = new Date(d + "T00:00:00");
  return `${dt.getMonth() + 1}/${dt.getDate()}`;
};
const diffDaysInclusive = (from: string, to: string) => {
  const start = new Date(from + "T00:00:00");
  const end = new Date(to + "T00:00:00");
  return Math.floor((end.getTime() - start.getTime()) / 86400000) + 1;
};
const getDates = (from: string, to: string): string[] => {
  const dates: string[] = [];
  let cur = from;
  while (cur <= to && dates.length < 50) {
    dates.push(cur);
    cur = addDays(cur, 1);
  }
  return dates;
};

function TaskIndicator({ task }: { task: DashboardTask }) {
  return (
    <div className="flex items-start gap-2">
      <div
        aria-hidden="true"
        className={`mt-0.5 flex h-4 w-4 flex-shrink-0 items-center justify-center rounded border ${
          task.done ? "border-slate-500 bg-slate-500 text-white" : "border-slate-300 bg-white"
        }`}
      >
        {task.done && (
          <svg className="h-3 w-3" viewBox="0 0 12 12" fill="none">
            <path d="M2 6l2.5 2.5L10 3" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        )}
      </div>
      <span className={`text-sm leading-6 break-words whitespace-normal ${task.done ? "text-slate-500 line-through" : "text-slate-700"}`}>
        {task.title}
      </span>
    </div>
  );
}

export default function Dashboard({ token }: { token: string }) {
  const [rows, setRows]         = useState<DashboardRow[] | null>(null);
  const [dateFrom, setDateFrom] = useState(addDays(today(), -3));
  const [dateTo, setDateTo]     = useState(addDays(today(), 7));
  const [error, setError]       = useState<string | null>(null);
  const [loading, setLoading]   = useState(false);

  useEffect(() => {
    if (!dateFrom || !dateTo) {
      return;
    }
    if (dateFrom > dateTo) {
      setRows(null);
      setError("開始日は終了日以前にしてください。");
      return;
    }
    if (diffDaysInclusive(dateFrom, dateTo) > 50) {
      setRows(null);
      setError("表示できる期間は最大50日です。");
      return;
    }
    setLoading(true);
    setError(null);
    setRows(null);
    fetchDashboard(token, dateFrom, dateTo)
      .then(setRows)
      .catch(() => setError("取得に失敗しました。バックエンドが起動しているか確認してください。"))
      .finally(() => setLoading(false));
  }, [token, dateFrom, dateTo]);

  const dates = rows !== null ? getDates(dateFrom, dateTo) : [];

  return (
    <div>
      <div className="mb-6">
        <p className="text-xs font-semibold uppercase tracking-widest text-blue-500 mb-1">
          DASHBOARD
        </p>
        <h2 className="text-2xl font-semibold text-slate-800">全社員タスク一覧</h2>
      </div>

      {/* 検索フォーム */}
      <div className="mb-5 rounded-xl border bg-white p-4 shadow-sm">
        <div className="flex flex-wrap items-end gap-3">
          <div>
            <label className="block text-xs font-medium text-slate-500 mb-1">開始日</label>
            <input
              type="date"
              value={dateFrom}
              onChange={e => setDateFrom(e.target.value)}
              className="rounded-lg border px-3 py-1.5 text-sm outline-none focus:border-blue-400"
            />
          </div>
          <div>
            <label className="block text-xs font-medium text-slate-500 mb-1">終了日</label>
            <input
              type="date"
              value={dateTo}
              onChange={e => setDateTo(e.target.value)}
              className="rounded-lg border px-3 py-1.5 text-sm outline-none focus:border-blue-400"
            />
          </div>
        </div>
        <p className="mt-2 text-xs text-slate-400">
          ※ 最大50日間まで表示できます
        </p>
      </div>

      {/* エラー */}
      {error && (
        <p className="mb-4 rounded-lg bg-red-50 px-4 py-2 text-sm text-red-600">
          {error}
        </p>
      )}

      {/* 読み込み中 */}
      {loading && (
        <div className="rounded-2xl border bg-white py-16 text-center">
          <p className="text-slate-400 text-sm">読み込み中...</p>
        </div>
      )}

      {/* ダッシュボード本体 */}
      {rows !== null && !loading && (
        <div className="overflow-x-auto rounded-2xl border bg-white shadow-sm">

          {/* 日付ヘッダー */}
          <div
            className="grid"
            style={{ gridTemplateColumns: `240px repeat(${dates.length}, minmax(180px, 1fr))` }}
          >
            <div className="border-r px-5 py-4 text-sm font-semibold text-slate-600">
              社員 / 日付
            </div>
            {dates.map(d => (
              <div
                key={d}
                className="border-r px-4 py-4 text-center text-sm font-semibold text-slate-600 last:border-r-0"
              >
                <div>{fmtDate(d)}</div>
                {d === today() && (
                  <div className="text-[11px] font-normal text-slate-400">今日</div>
                )}
              </div>
            ))}
          </div>

          {/* データなし */}
          {rows.length === 0 && (
            <p className="py-12 text-center text-sm text-slate-400">
              対象期間にタスクを持つ社員がいません
            </p>
          )}

          {/* 社員行 */}
          {rows.map(row => (
            <div
              key={row.employee_id}
              className="grid"
              style={{ gridTemplateColumns: `240px repeat(${dates.length}, minmax(180px, 1fr))` }}
            >
              {/* 社員名 */}
              <div className="border-r px-5 py-5">
                <p className="text-base font-medium text-slate-800">{row.name}</p>
                {row.department && (
                  <p className="mt-1 text-sm text-slate-400">{row.department}</p>
                )}
              </div>

              {/* 日付別タスク */}
              {dates.map(d => {
                const tasks = row.tasks_by_date[d] ?? [];
                return (
                  <div
                    key={d}
                    className="min-h-24 border-r px-4 py-4 align-top last:border-r-0"
                  >
                    {tasks.length === 0 ? (
                      <div className="min-h-16" />
                    ) : (
                      <ul className="space-y-3">
                        {tasks.map((task, i) => (
                          <li key={i} className="min-w-0">
                            <TaskIndicator task={task} />
                          </li>
                        ))}
                      </ul>
                    )}
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      )}

      {/* 凡例 */}
      {rows !== null && !loading && (
        <p className="mt-3 text-xs text-slate-400 text-right">
          チェックあり = 完了済みタスク
        </p>
      )}
    </div>
  );
}
