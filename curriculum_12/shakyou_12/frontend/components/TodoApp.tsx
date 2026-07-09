"use client";

/**
 * TodoApp.tsx
 * 役割: ToDoアプリのメインUIコンポーネント
 *
 * アプリ制作①のターミナルメニューをWeb画面に置き換えたもの:
 *   メニュー「1. 追加」  → 入力フォーム + 追加ボタン
 *   メニュー「2. 一覧」  → タスク一覧表示
 *   メニュー「3. 完了」  → チェックボックス or 完了ボタン
 *   メニュー「4. 削除」  → 削除ボタン
 */

import { useState, useEffect } from "react";
import { Task, fetchTasks, createTask, toggleTask, deleteTask } from "@/lib/api";

export default function TodoApp() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [input, setInput] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  // ── 起動時にタスク一覧を取得（アプリ制作①の load_tasks に対応）──
  useEffect(() => {
    fetchTasks()
      .then(setTasks)
      .catch(() => setError("バックエンドに接続できませんでした"))
      .finally(() => setLoading(false));
  }, []);

  // ── タスクを追加する（アプリ制作①の add_task に対応）────────────
  async function handleAdd(e: React.FormEvent) {
    e.preventDefault();
    const title = input.trim();
    if (!title) {
      setError("タスク名を入力してください");
      return;
    }
    try {
      const newTask = await createTask(title);
      setTasks((prev) => [...prev, newTask]);
      setInput("");
      setError(null);
    } catch {
      setError("タスクの追加に失敗しました");
    }
  }

  // ── 完了・未完了を切り替える（アプリ制作①の toggle_task に対応）──
  async function handleToggle(id: number) {
    try {
      const updated = await toggleTask(id);
      setTasks((prev) => prev.map((t) => (t.id === updated.id ? updated : t)));
    } catch {
      setError("更新に失敗しました");
    }
  }

  // ── タスクを削除する（アプリ制作①の delete_task に対応）──────────
  async function handleDelete(id: number) {
    try {
      await deleteTask(id);
      setTasks((prev) => prev.filter((t) => t.id !== id));
    } catch {
      setError("削除に失敗しました");
    }
  }

  // ── 統計情報の計算 ───────────────────────────────────────────────
  const total = tasks.length;
  const done = tasks.filter((t) => t.done).length;
  const undone = total - done;

  if (loading) {
    return (
      <p className="text-center text-slate-400">読み込み中...</p>
    );
  }

  return (
    <div className="rounded-2xl border bg-white p-6 shadow-sm">

      {/* ── 統計カード ─────────────────────────────────── */}
      <div className="mb-6 grid grid-cols-3 gap-3 text-center">
        {[
          { label: "全体", value: total },
          { label: "未完了", value: undone },
          { label: "完了", value: done },
        ].map(({ label, value }) => (
          <div key={label} className="rounded-xl border bg-slate-50 p-3">
            <p className="text-xs text-slate-500">{label}</p>
            <p className="text-2xl font-semibold text-slate-800">{value}</p>
          </div>
        ))}
      </div>

      {/* ── エラー表示 ─────────────────────────────────── */}
      {error && (
        <p className="mb-4 rounded-lg bg-red-50 px-4 py-2 text-sm text-red-600">
          {error}
        </p>
      )}

      {/* ── タスク追加フォーム ──────────────────────────── */}
      <form onSubmit={handleAdd} className="mb-6 flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="新しいタスクを入力..."
          className="flex-1 rounded-xl border px-4 py-2 text-sm outline-none focus:border-blue-400 focus:ring-2 focus:ring-blue-100"
        />
        <button
          type="submit"
          className="rounded-xl bg-blue-600 px-5 py-2 text-sm font-medium text-white hover:bg-blue-700 transition"
        >
          追加
        </button>
      </form>

      {/* ── タスク一覧 ──────────────────────────────────── */}
      {tasks.length === 0 ? (
        <p className="rounded-xl border border-dashed border-slate-200 py-8 text-center text-sm text-slate-400">
          タスクはまだありません
        </p>
      ) : (
        <ul className="space-y-2">
          {tasks.map((task) => (
            <li
              key={task.id}
              className={`flex items-center gap-3 rounded-xl border px-4 py-3 transition ${
                task.done ? "bg-slate-50 opacity-60" : "bg-white"
              }`}
            >
              {/* 完了チェックボックス */}
              <button
                onClick={() => handleToggle(task.id)}
                className={`flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full border-2 transition ${
                  task.done
                    ? "border-blue-500 bg-blue-500 text-white"
                    : "border-slate-300 hover:border-blue-400"
                }`}
                aria-label={task.done ? "未完了にする" : "完了にする"}
              >
                {task.done && (
                  <svg className="h-3 w-3" viewBox="0 0 12 12" fill="none">
                    <path
                      d="M2 6l3 3 5-5"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                )}
              </button>

              {/* タスク名 */}
              <span
                className={`flex-1 text-sm ${
                  task.done ? "line-through text-slate-400" : "text-slate-800"
                }`}
              >
                {task.title}
              </span>

              {/* ID表示（デバッグ用） */}
              <span className="text-xs text-slate-300">#{task.id}</span>

              {/* 削除ボタン */}
              <button
                onClick={() => handleDelete(task.id)}
                className="rounded-lg px-2 py-1 text-xs text-slate-400 hover:bg-red-50 hover:text-red-500 transition"
                aria-label="削除"
              >
                削除
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
