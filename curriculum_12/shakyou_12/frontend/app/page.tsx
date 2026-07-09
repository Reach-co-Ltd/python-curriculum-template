"use client";
import { useState, useEffect } from "react";
import { fetchTasks, createTask, toggleTask, deleteTask } from "@/lib/api";
import type { Task } from "@/lib/api";

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [input, setInput] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTasks()
      .then(setTasks)
      .catch(() => setError("タスクの取得に失敗しました"))
      .finally(() => setLoading(false));
  }, []);

  async function handleAdd(e: React.FormEvent) {
    e.preventDefault();
    if (!input.trim()) { setError("タスク名を入力してください"); return; }
    try {
      const t = await createTask(input.trim());
      setTasks(p => [...p, t]);
      setInput("");
      setError(null);
    } catch { setError("追加に失敗しました"); }
  }

  async function handleToggle(id: number) {
    try {
      const t = await toggleTask(id);
      setTasks(p => p.map(x => x.id === t.id ? t : x));
    } catch { setError("更新に失敗しました"); }
  }

  async function handleDelete(id: number) {
    try {
      await deleteTask(id);
      setTasks(p => p.filter(x => x.id !== id));
    } catch { setError("削除に失敗しました"); }
  }

  if (loading) return <p className="text-center text-slate-400 py-12">読み込み中...</p>;

  return (
    <div className="min-h-screen bg-slate-50">
      <header className="border-b bg-white px-6 py-4 shadow-sm">
        <div className="mx-auto max-w-2xl flex items-center gap-2">
          <span className="text-xl">📋</span>
          <span className="text-lg font-semibold text-blue-600">ToDoアプリ</span>
        </div>
      </header>

      <main className="mx-auto max-w-2xl px-4 py-8">
        {error && (
          <p className="mb-4 rounded-lg bg-red-50 px-4 py-2 text-sm text-red-600">{error}</p>
        )}

        <div className="rounded-2xl border bg-white p-6 shadow-sm mb-6">
          <form onSubmit={handleAdd} className="flex gap-2">
            <input
              type="text"
              value={input}
              onChange={e => setInput(e.target.value)}
              placeholder="タスク名を入力"
              className="flex-1 rounded-lg border px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-300"
            />
            <button
              type="submit"
              className="rounded-lg bg-blue-600 px-5 py-2 text-sm font-medium text-white hover:bg-blue-700 transition"
            >
              追加
            </button>
          </form>
        </div>

        <div className="rounded-2xl border bg-white shadow-sm divide-y">
          {tasks.length === 0 && (
            <p className="text-center text-slate-400 py-12 text-sm">タスクはありません</p>
          )}
          {tasks.map(task => (
            <div key={task.id} className="flex items-center gap-3 px-6 py-4">
              <button
                onClick={() => handleToggle(task.id)}
                className={`flex h-5 w-5 flex-shrink-0 items-center justify-center rounded border transition ${
                  task.done ? "border-blue-600 bg-blue-600 text-white" : "border-slate-300 bg-white"
                }`}
              >
                {task.done && (
                  <svg className="h-3 w-3" viewBox="0 0 12 12" fill="none">
                    <path d="M2 6l2.5 2.5L10 3" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                )}
              </button>
              <span className={`flex-1 text-sm ${task.done ? "text-slate-400 line-through" : "text-slate-700"}`}>
                {task.title}
              </span>
              <button
                onClick={() => handleDelete(task.id)}
                className="text-slate-400 hover:text-red-500 transition text-lg leading-none"
              >
                ×
              </button>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
