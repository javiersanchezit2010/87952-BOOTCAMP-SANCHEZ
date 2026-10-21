import { createFileRoute } from "@tanstack/react-router";
import { useEffect, useState, type FormEvent } from "react";
import { apiGet, apiPost, type Alumno } from "@/lib/api.functions";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Registro de Alumnos" },
      { name: "description", content: "Cliente elegante para consultar y cargar alumnos en tu API." },
      { property: "og:title", content: "Registro de Alumnos" },
      { property: "og:description", content: "Consultá y cargá alumnos en tu API." },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary" },
    ],
  }),
  component: Index,
});

const DEFAULT_URL = "https://4p08kk0p-5000.brs.devtunnels.ms/";
const empty = { legajo: "", nombre: "", apellido: "", fechaDeNacimiento: "" };

function Index() {
  const [base, setBase] = useState(DEFAULT_URL);
  const [alumnos, setAlumnos] = useState<Alumno[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searchId, setSearchId] = useState("");
  const [form, setForm] = useState(empty);
  const [msg, setMsg] = useState<{ ok: boolean; text: string } | null>(null);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem("api-base");
    if (saved) setBase(saved);
    load(saved ?? DEFAULT_URL);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function load(b = base, id = "") {
    setLoading(true);
    setError(null);
    try {
      localStorage.setItem("api-base", b);
      const r = await apiGet({ data: { base: b, path: id ? `alumnos/${id}` : "alumnos" } });
      setAlumnos(Array.isArray(r) ? r : [r]);
    } catch (e) {
      setError(e instanceof Error ? e.message : "No se pudo conectar");
      setAlumnos([]);
    } finally {
      setLoading(false);
    }
  }

  async function submit(e: FormEvent) {
    e.preventDefault();
    setSaving(true);
    setMsg(null);
    try {
      const alumno: Alumno = {
        nombre: form.nombre,
        apellido: form.apellido,
        fechaDeNacimiento: form.fechaDeNacimiento,
        ...(form.legajo ? { legajo: Number(form.legajo) } : {}),
      };
      await apiPost({ data: { base, alumno } });
      setMsg({ ok: true, text: `${form.nombre} ${form.apellido} fue agregado.` });
      setForm(empty);
      load();
    } catch (e) {
      setMsg({ ok: false, text: e instanceof Error ? e.message : "Error al guardar" });
    } finally {
      setSaving(false);
    }
  }

  return (
    <main className="relative min-h-screen bg-background">
      <div className="app-aurora" aria-hidden="true" />
      <div className="relative mx-auto max-w-6xl px-6 py-12">
        <header className="mb-10">
          <p className="eyebrow">Cliente API · Alumnos</p>
          <h1 className="font-display text-5xl md:text-6xl text-foreground mt-2">
            Registro de <em className="text-primary">alumnos</em>
          </h1>
        </header>

        <section className="panel mb-8 flex flex-col gap-3 md:flex-row md:items-end">
          <label className="flex-1">
            <span className="field-label">URL de la API</span>
            <input className="field" value={base} onChange={(e) => setBase(e.target.value)} />
          </label>
          <button className="btn-primary" onClick={() => load()} disabled={loading}>
            {loading ? "Conectando…" : "Conectar"}
          </button>
        </section>

        <div className="grid gap-8 lg:grid-cols-[1fr_360px]">
          <section className="panel">
            <div className="mb-5 flex flex-wrap items-center justify-between gap-3">
              <h2 className="font-display text-2xl text-foreground">
                Alumnos <span className="text-muted-foreground text-lg">({alumnos.length})</span>
              </h2>
              <form
                className="flex gap-2"
                onSubmit={(e) => {
                  e.preventDefault();
                  load(base, searchId.trim());
                }}
              >
                <input
                  className="field w-32"
                  placeholder="Legajo"
                  value={searchId}
                  onChange={(e) => setSearchId(e.target.value)}
                />
                <button className="btn-ghost" type="submit">Buscar</button>
                {searchId && (
                  <button className="btn-ghost" type="button" onClick={() => { setSearchId(""); load(); }}>
                    Todos
                  </button>
                )}
              </form>
            </div>

            {error && <p className="alert-error mb-4">{error}</p>}

            <div className="overflow-x-auto">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b text-xs uppercase tracking-widest text-muted-foreground">
                    <th className="py-3 pr-4">Legajo</th>
                    <th className="py-3 pr-4">Nombre</th>
                    <th className="py-3 pr-4">Apellido</th>
                    <th className="py-3">Nacimiento</th>
                  </tr>
                </thead>
                <tbody>
                  {alumnos.map((a, i) => (
                    <tr key={a.legajo ?? i} className="border-b last:border-0 transition-colors hover:bg-muted/60">
                      <td className="py-3 pr-4"><span className="badge">#{a.legajo}</span></td>
                      <td className="py-3 pr-4 font-medium text-foreground">{a.nombre}</td>
                      <td className="py-3 pr-4 text-foreground">{a.apellido}</td>
                      <td className="py-3 text-muted-foreground tabular-nums">{a.fechaDeNacimiento}</td>
                    </tr>
                  ))}
                  {!loading && !alumnos.length && !error && (
                    <tr><td colSpan={4} className="py-10 text-center text-muted-foreground">Sin alumnos</td></tr>
                  )}
                </tbody>
              </table>
            </div>
          </section>

          <aside className="panel h-fit">
            <h2 className="font-display text-2xl text-foreground mb-5">Nuevo alumno</h2>
            <form onSubmit={submit} className="flex flex-col gap-4">
              {([
                ["legajo", "Legajo (opcional)", "number"],
                ["nombre", "Nombre", "text"],
                ["apellido", "Apellido", "text"],
                ["fechaDeNacimiento", "Fecha de nacimiento", "date"],
              ] as const).map(([k, label, type]) => (
                <label key={k}>
                  <span className="field-label">{label}</span>
                  <input
                    className="field"
                    type={type}
                    required={k !== "legajo"}
                    value={form[k]}
                    onChange={(e) => setForm({ ...form, [k]: e.target.value })}
                  />
                </label>
              ))}
              <button className="btn-primary mt-2" disabled={saving}>
                {saving ? "Guardando…" : "Agregar alumno"}
              </button>
              {msg && <p className={msg.ok ? "alert-ok" : "alert-error"}>{msg.text}</p>}
            </form>
          </aside>
        </div>
      </div>
    </main>
  );
}
