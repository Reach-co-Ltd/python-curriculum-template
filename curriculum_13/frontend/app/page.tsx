"use client";
import { useState } from "react";
import { login, fetchMe } from "@/lib/api";
import type { Me } from "@/lib/api";
import MainApp from "@/components/MainApp";

export default function Home() {
  const [token, setToken] = useState<string | null>(null);
  const [me, setMe]       = useState<Me | null>(null);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError]   = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true); setError(null);
    try {
      const tok  = await login(email, password);
      const user = await fetchMe(tok);
      setToken(tok); setMe(user);
    } catch {
      setError("メールアドレスまたはパスワードが違います");
    } finally { setLoading(false); }
  }

  if (token && me) {
    return <MainApp token={token} me={me} onLogout={() => { setToken(null); setMe(null); }} />;
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50">
      <div className="w-full max-w-sm">
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-2 mb-1">
            <span className="text-2xl">📋</span>
            <span className="text-xl font-semibold text-blue-600">社内タスク管理システム</span>
          </div>
          <p className="text-xs text-slate-400">Staff Task Manager</p>
        </div>
        <div className="bg-white rounded-2xl border shadow-sm p-8">
          <h2 className="text-lg font-semibold text-slate-800 mb-6 text-center">ログイン</h2>
          {error && <p className="mb-4 rounded-lg bg-red-50 px-4 py-2 text-sm text-red-600 text-center">{error}</p>}
          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <label className="block text-xs font-medium text-slate-600 mb-1">メールアドレス</label>
              <input type="email" value={email} onChange={e => setEmail(e.target.value)} required placeholder="your@example.com"
                className="w-full rounded-xl border px-4 py-2.5 text-sm outline-none focus:border-blue-400 focus:ring-2 focus:ring-blue-100" />
            </div>
            <div>
              <label className="block text-xs font-medium text-slate-600 mb-1">パスワード</label>
              <input type="password" value={password} onChange={e => setPassword(e.target.value)} required placeholder="••••••••"
                className="w-full rounded-xl border px-4 py-2.5 text-sm outline-none focus:border-blue-400 focus:ring-2 focus:ring-blue-100" />
            </div>
            <button type="submit" disabled={loading}
              className="w-full rounded-xl bg-blue-600 py-2.5 text-sm font-medium text-white hover:bg-blue-700 disabled:opacity-50 transition">
              {loading ? "ログイン中..." : "ログイン"}
            </button>
          </form>
          <div className="mt-6 border-t pt-4 text-center">
            <p className="text-xs text-slate-400 mb-1">開発用アカウント</p>
            <p className="text-xs text-slate-500">管理者: admin@example.com / admin1234</p>
            <p className="text-xs text-slate-500">一般: tanaka@example.com / user1234</p>
          </div>
        </div>
      </div>
    </div>
  );
}
