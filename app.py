import streamlit as st
from pathlib import Path
from datetime import datetime

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FileForge Pro",
    page_icon="🗂️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

:root {
    --bg:        #0d0d0d;
    --surface:   #141414;
    --surface2:  #1a1a1a;
    --border:    #2a2a2a;
    --accent:    #c8f060;
    --accent2:   #60c8f0;
    --danger:    #f06060;
    --amber:     #f0c860;
    --text:      #e8e8e8;
    --muted:     #666;
    --radius:    12px;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Syne', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 60% 40% at 80% 10%, rgba(200,240,96,.08) 0%, transparent 70%),
        radial-gradient(ellipse 50% 35% at 10% 90%, rgba(96,200,240,.06) 0%, transparent 70%),
        var(--bg);
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* ── Hero ── */
.hero { text-align: center; padding: 3rem 1rem 1.4rem; }
.hero-tag {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: .72rem;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: var(--accent);
    border: 1px solid rgba(200,240,96,.35);
    border-radius: 99px;
    padding: .3rem 1rem;
    margin-bottom: 1.4rem;
}
.hero-title {
    font-size: clamp(2.6rem, 7vw, 4.5rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -.02em;
    margin: 0 0 .8rem;
    background: linear-gradient(135deg, var(--text) 30%, var(--accent) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1rem;
    color: var(--muted);
    font-family: 'Space Mono', monospace;
    margin: 0 0 1.6rem;
}

/* ── Stats strip ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: .7rem;
    max-width: 560px;
    margin: 0 auto 2rem;
}
.stat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: .9rem .6rem;
    text-align: center;
}
.stat-num {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.5rem;
    color: var(--accent);
    line-height: 1.1;
}
.stat-label {
    font-family: 'Space Mono', monospace;
    font-size: .68rem;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: .25rem;
}

/* ── Operation cards ── */
.op-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.1rem .8rem;
    text-align: center;
    transition: border-color .2s, transform .15s;
}
.op-card.active { border-color: var(--accent); background: rgba(200,240,96,.07); }
.op-label {
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--muted);
}
.op-card.active .op-label { color: var(--accent); }

/* ── Panel ── */
.panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem 2rem 2.5rem;
    margin-bottom: 1.5rem;
}
.panel-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: .6rem;
    color: var(--text);
}
.panel-title span { font-size: 1.4rem; }

/* ── Widget overrides ── */
[data-testid="stTextInput"] > div > div > input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: #1a1a1a !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: .9rem !important;
}
[data-testid="stTextInput"] > div > div > input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(200,240,96,.12) !important;
}
label[data-testid="stWidgetLabel"] p {
    font-family: 'Space Mono', monospace !important;
    font-size: .78rem !important;
    letter-spacing: .06em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    margin-bottom: .4rem !important;
}

.stButton > button {
    background: var(--accent) !important;
    color: #0d0d0d !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: .9rem !important;
    letter-spacing: .04em !important;
    padding: .6rem 1.8rem !important;
    transition: opacity .2s, transform .15s !important;
    width: 100%;
}
.stButton > button:hover { opacity: .88 !important; transform: translateY(-1px) !important; }

[data-testid="stDownloadButton"] > button {
    background: var(--surface2) !important;
    color: var(--accent2) !important;
    border: 1px solid rgba(96,200,240,.4) !important;
    border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important;
    font-weight: 700 !important;
    font-size: .78rem !important;
    width: 100%;
}
[data-testid="stDownloadButton"] > button:hover { border-color: var(--accent2) !important; opacity: .9; }

[data-testid="stRadio"] > div { flex-direction: row !important; gap: .8rem !important; flex-wrap: wrap !important; }
[data-testid="stRadio"] > div > label {
    background: #1a1a1a;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: .5rem 1.1rem;
    cursor: pointer;
    font-family: 'Space Mono', monospace;
    font-size: .8rem;
    transition: border-color .2s;
}
[data-testid="stRadio"] > div > label:hover { border-color: var(--accent); }

[data-testid="stCheckbox"] label p {
    font-family: 'Space Mono', monospace !important;
    font-size: .82rem !important;
    color: var(--text) !important;
    text-transform: none !important;
}

/* ── Alerts ── */
.msg-success, .msg-error, .msg-info, .msg-warn {
    border-radius: 10px;
    padding: .9rem 1.2rem;
    font-family: 'Space Mono', monospace;
    font-size: .85rem;
    margin-top: 1rem;
    display: flex;
    align-items: center;
    gap: .7rem;
}
.msg-success { background: rgba(200,240,96,.1);  border: 1px solid rgba(200,240,96,.3); color: var(--accent); }
.msg-error   { background: rgba(240,96,96,.1);   border: 1px solid rgba(240,96,96,.3);  color: var(--danger); }
.msg-info    { background: rgba(96,200,240,.1);  border: 1px solid rgba(96,200,240,.3); color: var(--accent2); }
.msg-warn    { background: rgba(240,200,96,.1);  border: 1px solid rgba(240,200,96,.3); color: var(--amber); }

/* ── File content / preview ── */
.file-content {
    background: #111;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    font-family: 'Space Mono', monospace;
    font-size: .85rem;
    color: var(--accent2);
    white-space: pre-wrap;
    word-break: break-word;
    line-height: 1.7;
    margin-top: 1rem;
    max-height: 300px;
    overflow-y: auto;
}

/* ── File list rows ── */
.file-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: .55rem .2rem;
    border-bottom: 1px solid var(--border);
    font-family: 'Space Mono', monospace;
    font-size: .82rem;
    color: #ccc;
}
.file-row:last-child { border-bottom: none; }
.file-meta { color: var(--muted); font-size: .74rem; }

/* ── Activity log ── */
.log-item {
    font-family: 'Space Mono', monospace;
    font-size: .76rem;
    color: var(--muted);
    padding: .3rem 0;
    border-bottom: 1px dashed var(--border);
}
.log-item:last-child { border-bottom: none; }
.log-item .log-dot { color: var(--accent); margin-right: .5rem; }

.divider { border: none; border-top: 1px solid var(--border); margin: 1.4rem 0; }

.footer {
    text-align: center;
    color: var(--muted);
    font-family: 'Space Mono', monospace;
    font-size: .72rem;
    padding: 2rem 0 3rem;
    letter-spacing: .05em;
}
</style>
""", unsafe_allow_html=True)


# ─── Helpers ──────────────────────────────────────────────────────────────────
def success(msg): st.markdown(f'<div class="msg-success">✅ {msg}</div>', unsafe_allow_html=True)
def error(msg):   st.markdown(f'<div class="msg-error">✗ {msg}</div>',   unsafe_allow_html=True)
def info(msg):    st.markdown(f'<div class="msg-info">ℹ {msg}</div>',    unsafe_allow_html=True)
def warn(msg):    st.markdown(f'<div class="msg-warn">⚠ {msg}</div>',    unsafe_allow_html=True)

BASE_DIR = Path("fileforge_files")
BASE_DIR.mkdir(exist_ok=True)

TEXT_EXTS = {".txt", ".md", ".csv", ".json", ".py", ".log", ".yaml", ".yml", ".ini", ".cfg"}

def safe_path(name: str) -> Path:
    return BASE_DIR / Path(name.strip()).name

def list_files():
    return [f for f in sorted(BASE_DIR.iterdir()) if f.is_file()]

def human_size(n):
    for unit in ["B", "KB", "MB"]:
        if n < 1024:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} GB"

def log_action(msg):
    if "activity_log" not in st.session_state:
        st.session_state.activity_log = []
    st.session_state.activity_log.insert(0, f"{datetime.now().strftime('%H:%M:%S')} — {msg}")
    st.session_state.activity_log = st.session_state.activity_log[:6]


# ─── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-tag">🗂 File Management System — Pro</div>
    <h1 class="hero-title">FileForge</h1>
    <p class="hero-sub">create · read · update · delete · search · preview — elegantly</p>
</div>
""", unsafe_allow_html=True)

# ─── Stats strip ──────────────────────────────────────────────────────────────
all_files = list_files()
total_size = sum(f.stat().st_size for f in all_files)
last_mod = max((f.stat().st_mtime for f in all_files), default=None)
last_mod_str = datetime.fromtimestamp(last_mod).strftime("%H:%M") if last_mod else "—"

st.markdown(f"""
<div class="stats-row">
    <div class="stat-card"><div class="stat-num">{len(all_files)}</div><div class="stat-label">files</div></div>
    <div class="stat-card"><div class="stat-num">{human_size(total_size)}</div><div class="stat-label">total size</div></div>
    <div class="stat-card"><div class="stat-num">{last_mod_str}</div><div class="stat-label">last activity</div></div>
</div>
""", unsafe_allow_html=True)


# ─── Operation Selector ────────────────────────────────────────────────────────
if "op" not in st.session_state:
    st.session_state.op = "Create"

ops = [("✦ Create", "Create"), ("◎ Read", "Read"), ("⟳ Update", "Update"),
       ("✕ Delete", "Delete"), ("▦ Manage", "Manage")]

cols = st.columns(len(ops))
for col, (label, key) in zip(cols, ops):
    with col:
        active = "active" if st.session_state.op == key else ""
        st.markdown(f'<div class="op-card {active}"><div class="op-label">{label}</div></div>', unsafe_allow_html=True)
        if st.button(key, key=f"btn_{key}", use_container_width=True):
            st.session_state.op = key
            st.rerun()

op = st.session_state.op
icons = {"Create": "✦", "Read": "◎", "Update": "⟳", "Delete": "✕", "Manage": "▦"}

st.markdown(f'<div class="panel"><div class="panel-title"><span>{icons[op]}</span> {op}</div>', unsafe_allow_html=True)

# ── CREATE ────────────────────────────────────────────────────────────────────
if op == "Create":
    filename = st.text_input("File name", placeholder="e.g.  notes.txt")
    content  = st.text_area("File content", placeholder="Start writing…", height=160)

    if st.button("Create File"):
        if not filename:
            error("Please enter a file name.")
        else:
            path = safe_path(filename)
            if path.exists():
                error(f"'{filename}' already exists. Choose a different name.")
            else:
                path.write_text(content)
                log_action(f"Created '{filename}'")
                success(f"'{filename}' created successfully!")

# ── READ ──────────────────────────────────────────────────────────────────────
elif op == "Read":
    files = [f.name for f in list_files()]
    if not files:
        info("No files yet. Create one first!")
    else:
        search = st.text_input("Search files", placeholder="type to filter…")
        filtered = [f for f in files if search.lower() in f.lower()] if search else files
        if not filtered:
            warn("No files match that search.")
        else:
            filename = st.selectbox("Select a file to read", filtered)
            path = safe_path(filename)
            ext = path.suffix.lower()

            c1, c2 = st.columns([1, 1])
            with c1:
                do_read = st.button("Read File")
            with c2:
                st.download_button("⬇ Download", data=path.read_bytes(), file_name=filename, use_container_width=True)

            if do_read:
                if ext not in TEXT_EXTS and ext != "":
                    warn(f"'{ext}' isn't previewed as text — download it to view the raw contents.")
                else:
                    content = path.read_text(errors="replace")
                    if content.strip():
                        st.markdown(f'<div class="file-content">{content}</div>', unsafe_allow_html=True)
                    else:
                        info("This file is empty.")

# ── UPDATE ────────────────────────────────────────────────────────────────────
elif op == "Update":
    files = [f.name for f in list_files()]
    if not files:
        info("No files yet. Create one first!")
    else:
        filename = st.selectbox("Select a file to update", files)
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        action = st.radio("Operation", ["Rename", "Append content", "Overwrite content", "Duplicate"], horizontal=True)

        if action == "Rename":
            new_name = st.text_input("New file name", placeholder="e.g.  renamed.txt")
            if st.button("Rename File"):
                if not new_name:
                    error("Please enter a new name.")
                elif safe_path(new_name).exists():
                    error(f"'{new_name}' already exists.")
                else:
                    safe_path(filename).rename(safe_path(new_name))
                    log_action(f"Renamed '{filename}' → '{new_name}'")
                    success(f"Renamed to '{new_name}' successfully!")
                    st.rerun()

        elif action == "Append content":
            data = st.text_area("Content to append", height=130)
            if st.button("Append"):
                if not data:
                    error("Nothing to append.")
                else:
                    with open(safe_path(filename), "a") as f:
                        f.write("\n" + data)
                    log_action(f"Appended to '{filename}'")
                    success("Content appended successfully!")

        elif action == "Overwrite content":
            current = safe_path(filename).read_text(errors="replace")
            data = st.text_area("New content (replaces everything)", value=current, height=160)
            if st.button("Overwrite File"):
                safe_path(filename).write_text(data)
                log_action(f"Overwrote '{filename}'")
                success("File overwritten successfully!")

        else:  # Duplicate
            stem, suffix = Path(filename).stem, Path(filename).suffix
            default_copy = f"{stem}_copy{suffix}"
            copy_name = st.text_input("Duplicate as", value=default_copy)
            if st.button("Duplicate File"):
                dest = safe_path(copy_name)
                if dest.exists():
                    error(f"'{copy_name}' already exists.")
                else:
                    dest.write_bytes(safe_path(filename).read_bytes())
                    log_action(f"Duplicated '{filename}' → '{copy_name}'")
                    success(f"Duplicated as '{copy_name}'!")
                    st.rerun()

# ── DELETE ────────────────────────────────────────────────────────────────────
elif op == "Delete":
    files = [f.name for f in list_files()]
    if not files:
        info("No files to delete.")
    else:
        mode = st.radio("Mode", ["Single file", "Bulk delete"], horizontal=True)

        if mode == "Single file":
            filename = st.selectbox("Select a file to delete", files)
            warn(f"This will permanently delete <b>{filename}</b>. This cannot be undone.")
            confirm = st.checkbox(f'I understand — delete "{filename}"')
            if st.button("Delete File"):
                if not confirm:
                    error("Please check the confirmation box first.")
                else:
                    safe_path(filename).unlink()
                    log_action(f"Deleted '{filename}'")
                    success(f"'{filename}' deleted successfully!")
                    st.rerun()
        else:
            selected = st.multiselect("Select files to delete", files)
            if selected:
                warn(f"This will permanently delete <b>{len(selected)}</b> file(s). This cannot be undone.")
                confirm = st.checkbox("I understand — delete all selected files")
                if st.button("Delete Selected"):
                    if not confirm:
                        error("Please check the confirmation box first.")
                    else:
                        for f in selected:
                            safe_path(f).unlink()
                        log_action(f"Bulk deleted {len(selected)} file(s)")
                        success(f"Deleted {len(selected)} file(s) successfully!")
                        st.rerun()

# ── MANAGE (browse / search / sort) ───────────────────────────────────────────
elif op == "Manage":
    files = list_files()
    if not files:
        info("Workspace is empty. Create a file to get started.")
    else:
        c1, c2 = st.columns([2, 1])
        with c1:
            search = st.text_input("Search", placeholder="filter by name…")
        with c2:
            sort_by = st.selectbox("Sort by", ["Name", "Size", "Modified"])

        filtered = [f for f in files if search.lower() in f.name.lower()] if search else files
        if sort_by == "Name":
            filtered = sorted(filtered, key=lambda f: f.name.lower())
        elif sort_by == "Size":
            filtered = sorted(filtered, key=lambda f: f.stat().st_size, reverse=True)
        else:
            filtered = sorted(filtered, key=lambda f: f.stat().st_mtime, reverse=True)

        if not filtered:
            warn("No files match that search.")
        else:
            for f in filtered:
                stat = f.stat()
                mtime = datetime.fromtimestamp(stat.st_mtime).strftime("%b %d, %H:%M")
                st.markdown(
                    f'<div class="file-row"><span>📄 {f.name}</span>'
                    f'<span class="file-meta">{human_size(stat.st_size)} · {mtime}</span></div>',
                    unsafe_allow_html=True,
                )

st.markdown("</div>", unsafe_allow_html=True)  # close .panel

# ─── Activity log ─────────────────────────────────────────────────────────────
if st.session_state.get("activity_log"):
    with st.expander("🕐  Recent activity", expanded=False):
        for entry in st.session_state.activity_log:
            st.markdown(f'<div class="log-item"><span class="log-dot">●</span>{entry}</div>', unsafe_allow_html=True)

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built with ♥ using Python & Streamlit &nbsp;·&nbsp; FileForge Pro
</div>
""", unsafe_allow_html=True)