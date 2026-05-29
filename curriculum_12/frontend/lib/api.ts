export type Task = {
  id: number;
  title: string;
  done: boolean;
  created_at: string;
};

const BASE = "/api";

export async function fetchTasks(): Promise<Task[]> {
  const res = await fetch(`${BASE}/tasks`, { cache: "no-store" });
  if (!res.ok) throw new Error("取得に失敗しました");
  return res.json();
}

export async function createTask(title: string): Promise<Task> {
  const res = await fetch(`${BASE}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  if (!res.ok) throw new Error("追加に失敗しました");
  return res.json();
}

export async function toggleTask(id: number): Promise<Task> {
  const res = await fetch(`${BASE}/tasks/${id}/toggle`, { method: "PATCH" });
  if (!res.ok) throw new Error("更新に失敗しました");
  return res.json();
}

export async function deleteTask(id: number): Promise<void> {
  await fetch(`${BASE}/tasks/${id}`, { method: "DELETE" });
}
