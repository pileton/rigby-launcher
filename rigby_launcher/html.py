import os

HOME = os.path.expanduser("~")

HTML_INDEX = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.cdnfonts.com/css/sf-pro-display');
*{margin:0;padding:0;box-sizing:border-box}

:root {
  --bg: #000000;
  --text: #ffffff;
  --placeholder: #a1a1a1;
  --button: rgba(12,12,12,0.55);
  --button-border: rgba(255,255,255,0.06);
  --icon: #a1a1aa;
  --toggle: #33C759;
  --slider: #0091FF;
  --element: rgba(10,10,10,0.45);
  --element-border: rgba(255,255,255,0.04);
  --card: rgba(10,10,10,0.45);
  --card-border: rgba(255,255,255,0.04);
  --overlay: rgba(0,0,0,0.85);
  --input-bg: rgba(13,13,13,0.5);
  --dropdown-bg: rgba(13,13,13,0.6);
  --hover: rgba(255,255,255,0.04);
  --hover-border: rgba(255,255,255,0.08);
  --dropdown-item: rgba(255,255,255,0.7);
  --dropdown-hover: rgba(255,255,255,0.06);
  --focus-border: rgba(255,255,255,0.15);
  --thumb: rgba(255,255,255,0.06);
}

.white {
  --bg: #ffffff;
  --text: #000000;
  --placeholder: #6b7280;
  --button: rgba(243,244,246,0.55);
  --button-border: rgba(0,0,0,0.08);
  --icon: #6b7280;
  --toggle: #33C759;
  --slider: #0091FF;
  --element: rgba(249,250,251,0.45);
  --element-border: rgba(0,0,0,0.06);
  --card: rgba(249,250,251,0.45);
  --card-border: rgba(0,0,0,0.06);
  --overlay: rgba(255,255,255,0.85);
  --input-bg: rgba(255,255,255,0.5);
  --dropdown-bg: rgba(255,255,255,0.6);
  --hover: rgba(0,0,0,0.04);
  --hover-border: rgba(0,0,0,0.1);
  --dropdown-item: rgba(0,0,0,0.6);
  --dropdown-hover: rgba(0,0,0,0.04);
  --focus-border: rgba(0,0,0,0.15);
  --thumb: rgba(0,0,0,0.08);
}
.white #titlebar { background: rgba(255,255,255,0.4); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-bottom: 1px solid rgba(0,0,0,0.06); }

html, body {
  height: 100%;
  background: var(--bg);
  color: var(--text);
  font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  font-size: 15px;
  overflow: hidden;
}

#titlebar { display: flex; align-items: center; height: 52px; padding: 0 20px; background: rgba(0,0,0,0.4); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-bottom: 1px solid rgba(255,255,255,0.04); flex-shrink: 0; }
.title-icon:hover { color: var(--text) !important; }
#spacer { flex: 1; }

#main {
  flex: 1; overflow: hidden;
  display: flex; flex-direction: column; align-items: center;
  justify-content: center;
  padding: 40px 32px;
}

#center-wrap {
  display: flex; flex-direction: column; align-items: center;
  width: 100%; max-width: 560px;
}

.hero { display: flex; align-items: center; gap: 14px; }

.version-picker .dropdown-btn { min-width: 140px; padding: 12px 16px; font-size: 14px; }
.version-picker .dropdown-menu { min-width: 160px; }

.dl-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 10px;
  padding: 16px 44px; font-size: 16px; font-weight: 600;
  border: 1px solid var(--button-border); border-radius: 14px;
  cursor: pointer; background: var(--button); color: #fff;
  font-family: inherit;
  backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
  transition: background 0.2s ease, border-color 0.2s ease, transform 0.15s ease;
}
.dl-btn:hover { background: var(--card); border-color: var(--button-border); }
.dl-btn:active { transform: scale(0.97); }
.dl-btn:disabled { opacity: 0.4; cursor: default; transform: none; }
.dl-btn:disabled:hover { background: var(--button); border-color: var(--button-border); }
.dl-btn svg { width: 22px; height: 22px; }

.icon-btn {
  display: inline-flex; align-items: center; justify-content: center;
  width: 48px; height: 48px; border: none; border-radius: 14px;
  cursor: pointer; background: transparent; color: var(--icon);
  backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
  transition: background 0.2s ease, color 0.2s ease, transform 0.15s ease;
}
.icon-btn:hover { background: var(--hover); color: var(--text); }
.icon-btn:active { transform: scale(0.92); }
#titlebar .icon-btn { color: var(--text); opacity: 0.8; }
#titlebar .icon-btn:hover { opacity: 1; }
.icon-btn svg { width: 22px; height: 22px; }
.icon-btn.active { color: var(--text); }
.icon-btn.active svg { transform: rotate(60deg); }
.icon-btn:disabled { opacity: 0.3; cursor: default; transform: none; }
.icon-btn:disabled:hover { background: transparent; color: var(--icon); }

.lucide { stroke: currentColor; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

#dl-progress { display: none; width: 100%; margin: 16px 0 0; }
#dl-progress.show { display: flex; }

#settings-area {
  width: 100%;
  display: flex; flex-direction: column; gap: 32px;
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  transition: max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s ease;
}
#settings-area.open {
  max-height: 5000px;
  opacity: 1;
  overflow: visible;
}

.section { display: flex; flex-direction: column; gap: 10px; }
.section-label { font-size: 13px; color: var(--placeholder); font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em; }

.element {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 16px; background: var(--element);
  border: 1px solid var(--element-border); border-radius: 14px;
  gap: 12px; min-height: 48px;
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  transition: border-color 0.2s ease;
}
.element:hover { border-color: var(--hover-border); }
.element-info { flex: 1; min-width: 0; }
.element-title { font-size: 14px; font-weight: 500; }
.element-desc { font-size: 12px; color: var(--placeholder); margin-top: 2px; }
.toggle { position: relative; width: 54px; height: 28px; cursor: pointer; flex-shrink: 0; }
.toggle input { display: none; }
.toggle-track {
  position: absolute; inset: 0;
  border-radius: 14px; transition: background 0.25s ease; background: var(--card);
}
.toggle-track::after {
  content: ''; position: absolute; width: 32px; height: 22px;
  border-radius: 11px; background: #fff;
  top: 3px; left: 2px;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  box-shadow: 0 1px 4px rgba(0,0,0,0.3);
}
.toggle input:checked + .toggle-track { background: var(--toggle); }
.toggle input:checked + .toggle-track::after { transform: translateX(18px); }

.slider-wrap { display: flex; align-items: center; gap: 12px; flex: 1; max-width: 260px; }
.slider-val { font-size: 13px; color: var(--placeholder); min-width: 32px; text-align: right; }
.c-slider { flex: 1; position: relative; height: 28px; display: flex; align-items: center; cursor: pointer; touch-action: none; overflow: hidden; border-radius: 10px; }
.c-slider-track { position: absolute; left: 0; right: 0; height: 7px; background: var(--card); border-radius: 10px; pointer-events: none; }
.c-slider-fill { position: absolute; left: 0; height: 7px; background: var(--slider); border-radius: 10px; pointer-events: none; transition: width 0.18s ease-out; }
.c-slider-thumb { position: absolute; width: 28px; height: 22px; background: #fff; border-radius: 11px; box-shadow: 0 1px 4px rgba(0,0,0,0.3); top: 50%; margin-top: -11px; pointer-events: none; transition: left 0.18s ease-out; }

.dropdown { position: relative; }
.dropdown-btn {
  display: flex; align-items: center; gap: 8px;
  padding: 12px 16px; background: var(--element);
  border: 1px solid var(--element-border); border-radius: 14px;
  color: var(--text); font-size: 14px; font-family: inherit;
  cursor: pointer; white-space: nowrap;
  transition: background 0.2s ease, border-color 0.2s ease;
}
.dropdown-btn:hover { background: var(--card); border-color: var(--button-border); }
.dropdown-btn:active { background: var(--hover); }
.dropdown-btn svg { width: 16px; height: 16px; margin-left: 4px; opacity: 0.6; }
.dropdown-menu {
  position: absolute; top: calc(100% + 6px); left: 0;
  min-width: 100%; background: var(--dropdown-bg);
  border: 1px solid var(--element-border); border-radius: 14px;
  padding: 4px; overflow: hidden; z-index: 100;
  opacity: 0; transform: translateY(-6px) scale(0.96);
  pointer-events: none;
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.dropdown-menu.open { opacity: 1; transform: translateY(0) scale(1); pointer-events: auto; }
.dropdown-item {
  padding: 10px 14px; font-size: 13px;
  color: var(--dropdown-item); cursor: pointer;
  border-radius: 10px;
  transition: background 0.15s ease, color 0.15s ease;
}
.dropdown-item:hover { background: var(--dropdown-hover); color: var(--text); }
.dropdown-item.selected { color: var(--slider); background: rgba(0,145,255,0.1); }

.progress-bar { width: 100%; height: 4px; background: var(--card); border-radius: 3px; overflow: hidden; }
.progress-fill { height: 100%; background: var(--slider); border-radius: 3px; transition: width 0.4s ease; }

.config-group { display: flex; flex-direction: column; gap: 12px; width: 100%; }
.config-row { display: flex; flex-direction: column; gap: 6px; }
.config-label { font-size: 13px; font-weight: 500; color: var(--placeholder); }
.config-input {
  padding: 10px 14px; background: var(--input-bg);
  border: 1px solid var(--element-border); border-radius: 12px;
  color: var(--text); font-size: 13px; font-family: inherit; outline: none;
  transition: border-color 0.2s ease;
}
.config-input:focus { border-color: var(--focus-border); }
.config-inline {
  display: flex; align-items: center; justify-content: space-between;
  padding: 6px 0;
}

#save-btn {
  padding: 12px; font-size: 14px; font-weight: 500; width: 100%;
  border: none; border-radius: 12px; cursor: pointer;
  background: var(--button); color: var(--text); font-family: inherit;
  transition: background 0.2s ease;
}
#save-btn:hover { background: var(--card); }
#save-btn:active { background: #282828; }
#save-btn svg { width: 18px; height: 18px; }

#fixer-overlay {
  position: fixed; inset: 0; z-index: 9999;
  background: var(--overlay);
  display: none; align-items: center; justify-content: center;
}
#fixer-overlay.open { display: flex; }
#fixer-card {
  background: var(--card); border: 1px solid var(--card-border);
  border-radius: 20px; padding: 40px 48px; text-align: center;
  min-width: 340px;
}
#fixer-icon { margin-bottom: 16px; }
.fixer-spinner {
  width: 44px; height: 44px; border: 3px solid var(--card);
  border-top: 3px solid var(--placeholder); border-radius: 50%;
  animation: fs 1s linear infinite; margin: 0 auto;
}
@keyframes fs { to { transform: rotate(360deg); } }
.fixer-check { color: var(--toggle); }
.fixer-check svg { width: 48px; height: 48px; }
#fixer-title { font-size: 18px; font-weight: 600; margin-bottom: 6px; }
#fixer-sub { font-size: 13px; color: var(--placeholder); }

.update-badge {
  display: none; align-items: center; gap: 6px;
  font-size: 12px; color: var(--slider); cursor: pointer;
  margin-left: 14px;
}
.update-badge.show { display: inline-flex; }
.update-badge svg { width: 14px; height: 14px; }

#cl-overlay {
  position: fixed; inset: 0; z-index: 9998;
  background: var(--overlay);
  display: none; align-items: center; justify-content: center;
}
#cl-overlay.open { display: flex; }
#cl-card {
  background: var(--card); border: 1px solid var(--card-border);
  border-radius: 20px; padding: 32px 36px; width: 420px; max-height: 70vh;
  overflow-y: auto; position: relative;
}
#cl-close {
  position: absolute; top: 16px; right: 16px;
  background: none; border: none; color: var(--icon); cursor: pointer;
  padding: 6px;
}
#cl-close:hover { color: var(--text); }
#cl-close svg { width: 20px; height: 20px; }
#cl-title { font-size: 20px; font-weight: 600; margin-bottom: 20px; padding-right: 30px; }
.cl-entry { margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--element-border); }
.cl-entry:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.cl-ver { font-size: 16px; font-weight: 600; color: var(--slider); margin-bottom: 4px; }
.cl-date { font-size: 12px; color: var(--placeholder); margin-bottom: 8px; }
.cl-item { font-size: 13px; color: var(--placeholder); margin-bottom: 6px; line-height: 1.5; }
.cl-item::before { content: '\\2022'; color: var(--slider); display: inline-block; width: 16px; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--thumb); border-radius: 3px; }

#acct-pill {
  display: flex; align-items: center; gap: 6px;
  padding: 4px 10px 4px 4px;
  border: 1px solid var(--element-border); border-radius: 20px;
  cursor: pointer; background: var(--element);
  transition: border-color 0.2s;
  font-size: 13px;
  max-width: 180px;
}
#acct-pill:hover { border-color: var(--hover-border); }
#acct-pill img { border-radius: 50%; object-fit: cover; background: var(--thumb); flex-shrink: 0; width: 22px; height: 22px; }
#acct-pill span { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.acct-drop {
  position: fixed; top: 52px; left: 8px; z-index: 9999;
  background: var(--card); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--card-border); border-radius: 14px;
  padding: 8px; min-width: 220px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
  flex-direction: column; gap: 4px;
  opacity: 0; transform: translateY(-6px) scale(0.96);
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.acct-drop.open { opacity: 1; transform: translateY(0) scale(1); pointer-events: auto; }
.acct-item {
  display: flex; align-items: center; gap: 10px;
  padding: 8px 10px; border-radius: 10px;
  cursor: pointer; transition: background 0.15s;
  font-size: 13px;
}
.acct-item:hover { background: var(--hover); }
.acct-item.active { color: var(--slider); font-weight: 600; }
.acct-item img { border-radius: 50%; object-fit: cover; width: 28px; height: 28px; background: var(--thumb); flex-shrink: 0; }
.acct-item .acct-remove {
  margin-left: auto; opacity: 0; transition: opacity 0.15s;
  color: #ef4444; background: none; border: none; cursor: pointer; padding: 4px;
}
.acct-item:hover .acct-remove { opacity: 1; }
.acct-add-btn {
  display: flex; align-items: center; justify-content: center; gap: 6px;
  padding: 10px; margin-top: 4px;
  border: 1px dashed var(--element-border); border-radius: 10px;
  background: none; color: var(--icon); cursor: pointer;
  font-family: inherit; font-size: 13px; transition: all 0.2s;
}
.acct-add-btn:hover { border-color: var(--slider); color: var(--slider); }
.acct-add-btn:disabled { opacity: 0.3; cursor: default; border-color: var(--element-border); color: var(--icon); }

#waves {
  position: fixed; inset: 0; z-index: 0;
  overflow: hidden; pointer-events: none !important;
}
#waves canvas {
  display: block;
  width: 100%; height: 100%;
  pointer-events: none !important;
}
#app { position: relative; z-index: 2; display: flex; flex-direction: column; height: 100vh; }
</style>
</head>
<body>
<div id="waves"></div>
<div id="app">
  <div id="titlebar">
  <div id="acct-pill" onclick="toggleAccts()">
    <img id="acct-pfp" src="" width="22" height="22">
    <span id="acct-name">Account</span>
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
  </div>
  <div id="acct-drop" class="acct-drop">
    <div id="acct-list"></div>
    <button id="acct-add-btn" class="acct-add-btn" onclick="addAccount()">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
      Add Account
    </button>
  </div>
    <div id="spacer"></div>
    <div class="update-badge" id="update-badge" onclick="updateToLatest()">
      <svg class="lucide" viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>
      Update available
    </div>
    <a href="https://github.com/pileton/rigby-launcher" target="_blank" class="title-icon" style="display:inline-flex;color:var(--icon);"><svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" stroke="none"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg></a>
  </div>

  <div id="main">
    <div id="center-wrap">
      <div class="hero">
        <div class="dropdown version-picker" id="ver-dd">
          <div class="dropdown-btn" onclick="toggleDropdown('ver-dd')">
            <span id="ver-lbl">17.4I</span>
            <svg class="lucide" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
          </div>
          <div class="dropdown-menu" id="ver-menu"></div>
        </div>

        <button class="dl-btn" id="dl-main" onclick="handleDownload()">
          <svg class="lucide" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download
        </button>

        <button class="icon-btn" id="gear-btn" onclick="toggleSettings()">
          <svg class="lucide" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        </button>

        <button class="icon-btn" onclick="toggleChangelog()">
          <svg class="lucide" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
        </button>
      </div>

      <div class="element" id="dl-progress">
        <div class="element-info"><div class="element-title" id="dl-label">Downloading...</div></div>
        <div style="width:180px">
          <div class="progress-bar"><div class="progress-fill" id="dl-fill"></div></div>
          <div style="font-size:11px;color:var(--placeholder);margin-top:3px;text-align:right" id="dl-pct">0%</div>
        </div>
      </div>

      <div id="settings-area">
        <div class="section">
          <div class="section-label">Configuration</div>
          <div class="config-group" style="background:var(--element);border:1px solid var(--element-border);border-radius:14px;padding:16px">

            <div class="config-inline">
              <div>
                <div style="font-size:14px;font-weight:500">Theme</div>
                <div style="font-size:12px;color:var(--placeholder);margin-top:2px">Dark or white interface</div>
              </div>
              <div class="dropdown" id="theme-dd" style="min-width:120px">
                <div class="dropdown-btn" onclick="toggleDropdown('theme-dd')" style="padding:8px 14px;font-size:13px">
                  <span id="theme-lbl">Dark</span>
                  <svg class="lucide" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
                </div>
                <div class="dropdown-menu">
                  <div class="dropdown-item selected" data-val="dark" onclick="selectTheme('dark')">Dark</div>
                  <div class="dropdown-item" data-val="white" onclick="selectTheme('white')">White</div>
                </div>
              </div>
            </div>

            <div class="config-inline" style="border-top:1px solid var(--element-border);padding-top:12px">
              <div>
                <div style="font-size:14px;font-weight:500">Auto-update</div>
                <div style="font-size:12px;color:var(--placeholder);margin-top:2px">Automatically download new versions</div>
              </div>
              <label class="toggle"><input type="checkbox" id="set-auto-update" onchange="saveSettings()"><div class="toggle-track"></div></label>
            </div>

            <div class="config-inline" style="border-top:1px solid var(--element-border);padding-top:12px">
              <div>
                <div style="font-size:14px;font-weight:500">Auto-launch</div>
                <div style="font-size:12px;color:var(--placeholder);margin-top:2px">Launch game after launcher opens</div>
              </div>
              <label class="toggle"><input type="checkbox" id="set-auto-launch" onchange="saveSettings()"><div class="toggle-track"></div></label>
            </div>

            <div class="element" style="border:none;border-radius:0;padding:8px 0;background:transparent;margin-top:2px">
              <div class="element-info">
                <div class="element-desc">Launch delay (seconds)</div>
              </div>
              <div class="slider-wrap">
                <div class="c-slider" id="csl-delay" data-value="5">
                  <div class="c-slider-track"></div>
                  <div class="c-slider-fill" style="width:16.6%"></div>
                  <div class="c-slider-thumb" style="left:calc(16.6% - 14px)"></div>
                </div>
                <span class="slider-val" id="csl-delay-v">5s</span>
              </div>
            </div>

            <div class="config-inline" style="border-top:1px solid var(--element-border);padding-top:12px">
              <div>
                <div style="font-size:14px;font-weight:500">Itch Login Fixer</div>
                <div style="font-size:12px;color:var(--placeholder);margin-top:2px">Authorize itch.io for game access</div>
              </div>
              <button onclick="runFixer()" style="padding:8px 16px;font-size:13px;background:var(--input-bg);border:1px solid var(--element-border);border-radius:10px;color:var(--text);cursor:pointer;font-family:inherit;transition:background 0.2s" onmouseover="this.style.background='var(--hover)'" onmouseout="this.style.background=''">
                <svg class="lucide" viewBox="0 0 24 24" style="width:14px;height:14px;margin-right:6px;vertical-align:middle"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                Run Fixer
              </button>
            </div>


            <div class="config-row" style="border-top:1px solid var(--element-border);padding-top:12px">
              <div class="config-label">Game Directory</div>
              <div style="display:flex;gap:6px">
                <input class="config-input" type="text" id="set-game-dir" style="flex:1" placeholder="Select..." onblur="saveSettings()">
                <button class="icon-btn" onclick="browseGameDir()" style="width:42px;height:42px;flex-shrink:0;border:1px solid var(--element-border);border-radius:12px">
                  <svg class="lucide" viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>
                </button>
              </div>
            </div>
            <div class="config-row">
              <div class="config-label">Wine Prefix</div>
              <input class="config-input" type="text" id="set-wine-prefix" placeholder="/home/user/.wine-au" onblur="saveSettings()">
            </div>
            <div class="config-row">
              <div class="config-label">Wine Binary</div>
              <input class="config-input" type="text" id="set-wine-bin" placeholder="wine" onblur="saveSettings()">
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div id="cl-overlay">
  <div id="cl-card">
    <button id="cl-close" onclick="toggleChangelog()">
      <svg class="lucide" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
    <div id="cl-title">Changelog</div>
    <div class="cl-entry">
      <div class="cl-ver">v0.4</div>
      <div class="cl-date">August 2026</div>
      <div class="cl-item">Added missing v0.3 changelog</div>
      <div class="cl-item">Fixed several visual bugs in the ui</div>
      <div class="cl-item">Fixed launcher updating</div>
      <div class="cl-item">Fixed itch.io pfp not showing</div>
      <div class="cl-item">Added new themes</div>
      <div class="cl-item">Improved perfomance (launcher)</div>
    </div>
    <div class="cl-entry">
      <div class="cl-ver">v0.3</div>
      <div class="cl-date">August 2026</div>
      <div class="cl-item">Added newest game version 18I</div>
      <div class="cl-item">Removed useless text in code</div>
    </div>
    <div class="cl-entry">
      <div class="cl-ver">v0.2</div>
      <div class="cl-date">July 2026</div>
      <div class="cl-item">Account switching with itch.io OAuth</div>
      <div class="cl-item">Installation directory picker</div>
      <div class="cl-item">Game directory auto-detect and save</div>
      <div class="cl-item">Improved launch reliability with stripped env</div>
      <div class="cl-item">DXVK support for AMD graphics</div>
      <div class="cl-item">GitHub icon in title bar</div>
    </div>
    <div class="cl-entry">
      <div class="cl-ver">v0.1</div>
      <div class="cl-date">Initial release</div>
      <div class="cl-item">First release of the launcher</div>
    </div>
  </div>
</div>

<div id="fixer-overlay">
  <div id="fixer-card">
    <div id="fixer-icon"><div class="fixer-spinner"></div></div>
    <div id="fixer-title">Connecting to Itch.io</div>
    <div id="fixer-sub">Complete authorization in your browser</div>
  </div>
</div>

<script type="module">
import { Renderer, Program, Mesh, Triangle } from 'https://esm.sh/ogl@1.0.11';

function hexToVec3(hex) {
  const h = hex.replace('#', '');
  return [
    parseInt(h.slice(0, 2), 16) / 255,
    parseInt(h.slice(2, 4), 16) / 255,
    parseInt(h.slice(4, 6), 16) / 255
  ];
}

const vertexShader = `attribute vec2 uv; attribute vec2 position; varying vec2 vUv; void main() { vUv = uv; gl_Position = vec4(position, 0, 1); }`;

const fragmentShader = `precision highp float;

uniform float uTime;
uniform vec3 uResolution;
uniform float uSpeed;
uniform float uInnerLines;
uniform float uOuterLines;
uniform float uWarpIntensity;
uniform float uRotation;
uniform float uEdgeFadeWidth;
uniform float uColorCycleSpeed;
uniform float uBrightness;
uniform vec3 uColor1;
uniform vec3 uColor2;
uniform vec3 uColor3;
uniform vec2 uMouse;
uniform float uMouseInfluence;
uniform bool uEnableMouse;

#define HALF_PI 1.5707963

float hashF(float n) { return fract(sin(n * 127.1) * 43758.5453123); }

float smoothNoise(float x) {
  float i = floor(x); float f = fract(x);
  float u = f * f * (3.0 - 2.0 * f);
  return mix(hashF(i), hashF(i + 1.0), u);
}

float displaceA(float coord, float t) {
  float result = sin(coord * 2.123) * 0.2;
  result += sin(coord * 3.234 + t * 4.345) * 0.1;
  result += sin(coord * 0.589 + t * 0.934) * 0.5;
  return result;
}

float displaceB(float coord, float t) {
  float result = sin(coord * 1.345) * 0.3;
  result += sin(coord * 2.734 + t * 3.345) * 0.2;
  result += sin(coord * 0.189 + t * 0.934) * 0.3;
  return result;
}

vec2 rotate2D(vec2 p, float angle) {
  float c = cos(angle); float s = sin(angle);
  return vec2(p.x * c - p.y * s, p.x * s + p.y * c);
}

void main() {
  vec2 coords = gl_FragCoord.xy / uResolution.xy;
  coords = coords * 2.0 - 1.0;
  coords = rotate2D(coords, uRotation);

  float halfT = uTime * uSpeed * 0.5;
  float fullT = uTime * uSpeed;

  float mouseWarp = 0.0;
  if (uEnableMouse) {
    vec2 mPos = rotate2D(uMouse * 2.0 - 1.0, uRotation);
    float mDist = length(coords - mPos);
    mouseWarp = uMouseInfluence * exp(-mDist * mDist * 4.0);
  }

  float warpAx = coords.x + displaceA(coords.y, halfT) * uWarpIntensity + mouseWarp;
  float warpAy = coords.y - displaceA(coords.x * cos(fullT) * 1.235, halfT) * uWarpIntensity;
  float warpBx = coords.x + displaceB(coords.y, halfT) * uWarpIntensity + mouseWarp;
  float warpBy = coords.y - displaceB(coords.x * sin(fullT) * 1.235, halfT) * uWarpIntensity;

  vec2 fieldA = vec2(warpAx, warpAy);
  vec2 fieldB = vec2(warpBx, warpBy);
  vec2 blended = mix(fieldA, fieldB, mix(fieldA, fieldB, 0.5));

  float fadeTop = smoothstep(uEdgeFadeWidth, uEdgeFadeWidth + 0.4, blended.y);
  float fadeBottom = smoothstep(-uEdgeFadeWidth, -(uEdgeFadeWidth + 0.4), blended.y);
  float vMask = 1.0 - max(fadeTop, fadeBottom);

  float tileCount = mix(uOuterLines, uInnerLines, vMask);
  float scaledY = blended.y * tileCount;
  float nY = smoothNoise(abs(scaledY));

  float ridge = pow(
    step(abs(nY - blended.x) * 2.0, HALF_PI) * cos(2.0 * (nY - blended.x)),
    5.0
  );

  float lines = 0.0;
  for (float i = 1.0; i < 3.0; i += 1.0) {
    lines += pow(max(fract(scaledY), fract(-scaledY)), i * 2.0);
  }

  float pattern = vMask * lines;

  float cycleT = fullT * uColorCycleSpeed;
  float rChannel = (pattern + lines * ridge) * (cos(blended.y + cycleT * 0.234) * 0.5 + 1.0);
  float gChannel = (pattern + vMask * ridge) * (sin(blended.x + cycleT * 1.745) * 0.5 + 1.0);
  float bChannel = (pattern + lines * ridge) * (cos(blended.x + cycleT * 0.534) * 0.5 + 1.0);

  vec3 col = (rChannel * uColor1 + gChannel * uColor2 + bChannel * uColor3) * uBrightness;
  float alpha = clamp(length(col), 0.0, 1.0);

  gl_FragColor = vec4(col, alpha);
}`;

const container = document.getElementById('waves');
const renderer = new Renderer({ alpha: true, premultipliedAlpha: false, webgl2: false });
const gl = renderer.gl;
gl.clearColor(0, 0, 0, 0);

let program;
let currentMouse = [0.5, 0.5];
let targetMouse = [0.5, 0.5];

function handleMouseMove(e) {
  const rect = gl.canvas.getBoundingClientRect();
  targetMouse = [
    (e.clientX - rect.left) / rect.width,
    1.0 - (e.clientY - rect.top) / rect.height
  ];
}
function handleMouseLeave() {
  targetMouse = [0.5, 0.5];
}

function resize() {
  renderer.setSize(container.offsetWidth, container.offsetHeight);
  if (program) {
    program.uniforms.uResolution.value = [gl.canvas.width, gl.canvas.height, gl.canvas.width / gl.canvas.height];
  }
}
window.addEventListener('resize', resize);
resize();

const geometry = new Triangle(gl);
const rotationRad = (-45 * Math.PI) / 180;
program = new Program(gl, {
  vertex: vertexShader,
  fragment: fragmentShader,
  uniforms: {
    uTime: { value: 0 },
    uResolution: { value: [gl.canvas.width, gl.canvas.height, gl.canvas.width / gl.canvas.height] },
    uSpeed: { value: 0.3 },
    uInnerLines: { value: 35 },
    uOuterLines: { value: 36 },
    uWarpIntensity: { value: 1 },
    uRotation: { value: rotationRad },
    uEdgeFadeWidth: { value: 0 },
    uColorCycleSpeed: { value: 1 },
    uBrightness: { value: 0.2 },
    uColor1: { value: hexToVec3('#ffffff') },
    uColor2: { value: hexToVec3('#ffffff') },
    uColor3: { value: hexToVec3('#ffffff') },
    uMouse: { value: new Float32Array([0.5, 0.5]) },
    uMouseInfluence: { value: 2 },
    uEnableMouse: { value: true }
  }
});

const mesh = new Mesh(gl, { geometry, program });
  gl.canvas.style.pointerEvents = 'none';
container.appendChild(gl.canvas);

gl.canvas.addEventListener('mousemove', handleMouseMove);
gl.canvas.addEventListener('mouseleave', handleMouseLeave);

function update(time) {
  requestAnimationFrame(update);
  program.uniforms.uTime.value = time * 0.001;

  currentMouse[0] += 0.05 * (targetMouse[0] - currentMouse[0]);
  currentMouse[1] += 0.05 * (targetMouse[1] - currentMouse[1]);
  program.uniforms.uMouse.value[0] = currentMouse[0];
  program.uniforms.uMouse.value[1] = currentMouse[1];

  renderer.render({ scene: mesh });
}
requestAnimationFrame(update);
</script>
<script>
let state = {};
let dlInterval = null;
let settingsOpen = false;
let downloading = false;
let launching = false;
let fixerRunning = false;
let autoLaunchTimer = null;

function $(id) { return document.getElementById(id); }

function toggleSettings() {
  settingsOpen = !settingsOpen;
  $('settings-area').classList.toggle('open', settingsOpen);
  $('gear-btn').classList.toggle('active', settingsOpen);
  $('main').style.overflow = settingsOpen ? 'auto' : 'hidden';
  if (settingsOpen) refreshStatus();
}

function toggleDropdown(id) {
  document.querySelectorAll('.dropdown-menu.open').forEach(m => {
    if (!m.closest('.dropdown') || m.closest('.dropdown').id !== id) m.classList.remove('open');
  });
  document.querySelector('#' + id + ' .dropdown-menu').classList.toggle('open');
}

function selectDD(id, val) {
  const menu = document.querySelector('#' + id + ' .dropdown-menu');
  menu.querySelectorAll('.dropdown-item').forEach(e => e.classList.remove('selected'));
  menu.querySelector('.dropdown-item[data-val="' + val + '"]').classList.add('selected');
  menu.closest('.dropdown').querySelector('.dropdown-btn span').textContent = val;
  menu.classList.remove('open');
}

function selectVer(val) { selectDD('ver-dd', val); }

function selectTheme(val) {
  selectDD('theme-dd', val);
  if (val === 'white') document.documentElement.classList.add('white');
  else document.documentElement.classList.remove('white');
  saveSettings();
}

document.addEventListener('click', function(e) {
  document.querySelectorAll('.dropdown-menu.open').forEach(menu => {
    if (!menu.closest('.dropdown') || !menu.closest('.dropdown').contains(e.target)) menu.classList.remove('open');
  });
});

document.querySelectorAll('.c-slider').forEach(sl => {
  const fill = sl.querySelector('.c-slider-fill');
  const thumb = sl.querySelector('.c-slider-thumb');
  const valEl = document.getElementById(sl.id + '-v');
  let dragging = false;

  function pct(clientX) {
    const r = sl.getBoundingClientRect();
    return Math.max(0, Math.min(100, Math.round(((clientX - r.left) / r.width) * 100)));
  }

  function setPct(p) {
    sl.dataset.value = p;
    fill.style.width = p + '%';
    thumb.style.left = 'calc(' + p + '% - 14px)';
    if (valEl && sl.id === 'csl-delay') {
      const sec = Math.max(1, Math.round(p / 100 * 30));
      valEl.textContent = sec + 's';
      sl.dataset.seconds = sec;
    } else if (valEl) {
      valEl.textContent = p + '%';
    }
  }

  sl.addEventListener('mousedown', e => { e.preventDefault(); setPct(pct(e.clientX)); dragging = true; });
  document.addEventListener('mousemove', e => { if (!dragging) return; const p = pct(e.clientX); setPct(p); });
  document.addEventListener('mouseup', () => { dragging = false; saveSettings(); });
  sl.addEventListener('touchstart', e => { e.preventDefault(); setPct(pct(e.touches[0].clientX)); dragging = true; }, { passive: false });
  document.addEventListener('touchmove', e => { if (!dragging) return; const p = pct(e.touches[0].clientX); setPct(p); }, { passive: false });
  document.addEventListener('touchend', () => { dragging = false; saveSettings(); });
});

function setBtnState(mode) {
  const btn = $('dl-main');
  btn.className = 'dl-btn';
  if (mode === 'download') {
    btn.innerHTML = '<svg class="lucide" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download';
  } else if (mode === 'cancel') {
    btn.innerHTML = '<svg class="lucide" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> Cancel';
  } else if (mode === 'play') {
    btn.innerHTML = '<svg class="lucide" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg> Play';
  }
}

function showFixerOverlay(title, sub, done) {
  $('fixer-overlay').classList.add('open');
  $('fixer-icon').innerHTML = done
    ? '<div class="fixer-check"><svg class="lucide" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>'
    : '<div class="fixer-spinner"></div>';
  $('fixer-title').textContent = title;
  $('fixer-sub').textContent = sub;
}

function hideFixerOverlay() { $('fixer-overlay').classList.remove('open'); }

function toggleChangelog() { $('cl-overlay').classList.toggle('open'); }

async function runFixer() {
  if (fixerRunning) return;
  fixerRunning = true;
  showFixerOverlay('Connecting to Itch.io', 'Complete authorization in your browser', false);
  try {
    await fetch('/api/fixer/login', { method: 'POST' });
    let waited = 0;
    while (waited < 120) {
      await new Promise(r => setTimeout(r, 1000));
      waited++;
      const r = await fetch('/api/fixer/status');
      const d = await r.json();
      if (d.logged_in) {
        showFixerOverlay('Authorization Complete', 'Itch login saved successfully', true);
        await new Promise(r => setTimeout(r, 2000));
        break;
      }
    }
  } catch(e) {}
  hideFixerOverlay();
  fixerRunning = false;
  refreshStatus();
}

async function loadVersions() {
  try {
    const r = await fetch('/api/versions');
    const d = await r.json();
    const menu = $('ver-menu');
    menu.innerHTML = '';
    d.versions.forEach(v => {
      const item = document.createElement('div');
      item.className = 'dropdown-item' + (v === d.selected ? ' selected' : '');
      item.dataset.val = v;
      item.textContent = v;
      item.onclick = function() { selectVer(v); };
      menu.appendChild(item);
    });
    $('ver-lbl').textContent = d.selected;
  } catch(e) {}
}

async function checkGameStatus() {
  try {
    const r = await fetch('/api/status');
    state = await r.json();
    if (state.settings?.theme === 'white') {
      document.documentElement.classList.add('white');
    }
    if (state.latest_release && state.latest_release !== state.selected_version) {
      $('update-badge').classList.add('show');
      if (state.settings?.auto_update && !downloading && !state.game_installed) {
        updateToLatest();
      }
    } else {
      $('update-badge').classList.remove('show');
    }
    const verMatch = state.game_installed && state.installed_version === state.selected_version;
    if (verMatch && !downloading) {
      setBtnState('play');
    } else if (!downloading) {
      setBtnState('download');
    }
    if (state.settings?.auto_launch && state.game_installed && !autoLaunchTimer) {
      const delay = (state.settings.launch_delay || 5) * 1000;
      autoLaunchTimer = setTimeout(() => {
        autoLaunchTimer = null;
        if (!launching && state.wine_available) handlePlay();
      }, delay);
    }
  } catch(e) {}
}

async function updateToLatest() {
  if (!state.latest_release) return;
  const menu = $('ver-menu');
  const items = menu.querySelectorAll('.dropdown-item');
  let found = false;
  items.forEach(item => {
    if (item.dataset.val === state.latest_release) {
      selectVer(state.latest_release);
      found = true;
    }
  });
  if (found) {
    $('update-badge').classList.remove('show');
    handleDownload();
  }
}

async function handlePlay() {
  if (!state.wine_available || launching) return;
  if (!state.fixer?.logged_in && !fixerRunning) {
    $('dl-main').disabled = true;
    await runFixer();
    $('dl-main').disabled = false;
  }
  if (launching) return;
  launching = true;
  $('dl-main').disabled = true;
  try { await fetch('/api/launch', { method: 'POST' }); } catch(e) {}
  $('dl-main').disabled = false;
  launching = false;
}

async function handleDownload() {
  const btn = $('dl-main');

  if (dlInterval) { clearInterval(dlInterval); dlInterval = null; }

  if (downloading) {
    try { await fetch('/api/download/cancel', { method: 'POST' }); } catch(e) {}
    $('dl-progress').classList.remove('show');
    $('dl-fill').style.width = '0%';
    downloading = false;
    checkGameStatus();
    loadAccts();
    return;
  }

  if (state.game_installed && state.installed_version === $('ver-lbl').textContent.trim()) {
    if (autoLaunchTimer) { clearTimeout(autoLaunchTimer); autoLaunchTimer = null; }
    await handlePlay();
    return;
  }

  try {
    const version = $('ver-lbl').textContent.trim();
    await fetch('/api/download', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ version }) });
    downloading = true;
    setBtnState('cancel');
    $('dl-progress').classList.add('show');

    dlInterval = setInterval(async () => {
      try {
        const r = await fetch('/api/status');
        const d = await r.json();
        if (!d.downloading) {
          clearInterval(dlInterval); dlInterval = null;
          $('dl-progress').classList.remove('show');
          $('dl-fill').style.width = '0%';
          downloading = false;
          state = d;
          if (d.game_installed) setBtnState('play');
          else setBtnState('download');
          return;
        }
        const p = d.download_progress?.progress || 0;
        $('dl-fill').style.width = p + '%';
        $('dl-pct').textContent = p + '%';
        $('dl-label').textContent = d.download_progress?.extracting ? 'Extracting...' : 'Downloading...';
      } catch(e) {}
    }, 500);
  } catch(e) {}
}

async function refreshStatus() {
  try {
    const r = await fetch('/api/status');
    state = await r.json();
    const s = state.settings || {};
    $('set-game-dir').value = s.game_dir || '';
    $('set-wine-prefix').value = s.wine_prefix || '';
    $('set-wine-bin').value = s.wine_binary || 'wine';
    $('set-auto-update').checked = s.auto_update === true;
    $('set-auto-launch').checked = s.auto_launch === true;
    const theme = s.theme || 'dark';
    $('theme-lbl').textContent = theme.charAt(0).toUpperCase() + theme.slice(1);
    const themeMenuItems = document.querySelectorAll('#theme-dd .dropdown-item');
    themeMenuItems.forEach(i => i.classList.toggle('selected', i.dataset.val === theme));
    if (theme === 'white') document.documentElement.classList.add('white');
    else document.documentElement.classList.remove('white');
    const delay = s.launch_delay || 5;
    const dp = Math.round(delay / 30 * 100);
    const dsl = $('csl-delay');
    if (dsl) {
      dsl.dataset.value = dp;
      dsl.dataset.seconds = delay;
      dsl.querySelector('.c-slider-fill').style.width = dp + '%';
      dsl.querySelector('.c-slider-thumb').style.left = 'calc(' + dp + '% - 14px)';
      const ve = $('csl-delay-v');
      if (ve) ve.textContent = delay + 's';
    }
    if (!downloading) checkGameStatus();
    loadAccts();
  } catch(e) {}
}

async function browseGameDir() {
  try { const r = await fetch('/api/browse', { method: 'POST' }); const d = await r.json(); if (d.dir) $('set-game-dir').value = d.dir; } catch(e) {}
}

async function saveSettings() {
  try {
    await fetch('/api/settings', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        game_dir: $('set-game-dir').value,
        wine_prefix: $('set-wine-prefix').value,
        wine_binary: $('set-wine-bin').value,
        auto_update: $('set-auto-update').checked,
        auto_launch: $('set-auto-launch').checked,
        theme: $('theme-lbl').textContent.trim().toLowerCase(),
        launch_delay: parseInt(($('csl-delay')?.dataset.seconds) || 5),
      })
    });
  } catch(e) {}
}


async function toggleAccts() {
  var dd = document.getElementById('acct-drop');
  dd.classList.toggle('open');
}

document.addEventListener('click', function(e) {
  var dd = document.getElementById('acct-drop');
  var pill = document.getElementById('acct-pill');
  if (!pill.contains(e.target) && !dd.contains(e.target)) {
    dd.classList.remove('open');
  }
});

async function loadAccts() {
  try {
    var r = await fetch('/api/accounts');
    var d = await r.json();
    var list = document.getElementById('acct-list');
    list.innerHTML = '';
    var pillImg = document.getElementById('acct-pfp');
    var pillName = document.getElementById('acct-name');
    var activeFound = false;
    d.accounts.forEach(function(acc) {
      var item = document.createElement('div');
      item.className = 'acct-item';
      if (acc.active) {
        item.classList.add('active');
        activeFound = true;
        if (acc.avatar_url) pillImg.src = acc.avatar_url;
        else pillImg.src = '';
        pillName.textContent = acc.username || 'Account';
      }
      var img = document.createElement('img');
      img.src = acc.avatar_url || '';
      img.width = 28;
      img.height = 28;
      item.appendChild(img);
      var span = document.createElement('span');
      span.textContent = acc.username || 'Unknown';
      item.appendChild(span);
      if (acc.active) {
        var check = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        check.setAttribute('width', '16');
        check.setAttribute('height', '16');
        check.setAttribute('viewBox', '0 0 24 24');
        check.setAttribute('fill', 'none');
        check.setAttribute('stroke', 'currentColor');
        check.setAttribute('stroke-width', '2');
        var poly = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        poly.setAttribute('points', '20 6 9 17 4 12');
        check.appendChild(poly);
        item.appendChild(check);
      }
      var removeBtn = document.createElement('button');
      removeBtn.className = 'acct-remove';
      removeBtn.textContent = '\u2715';
      (function(tok) {
        removeBtn.onclick = function(e) { e.stopPropagation(); removeAccount(tok); };
      })(acc.token);
      item.appendChild(removeBtn);
      (function(tok) {
        item.onclick = function() { switchAccount(tok); };
      })(acc.token);
      list.appendChild(item);
    });
    if (!activeFound && d.accounts.length > 0) {
      pillImg.src = d.accounts[0].avatar_url || '';
      pillName.textContent = d.accounts[0].username || 'Account';
    }
    if (!activeFound && d.accounts.length === 0) {
      pillImg.src = '';
      pillName.textContent = 'Account';
    }
    var addBtn = document.getElementById('acct-add-btn');
    addBtn.disabled = d.accounts.length >= d.max;
  } catch(e) {}
}

async function addAccount() {
  try {
    var r = await fetch('/api/accounts/add', { method: 'POST' });
    var d = await r.json();
    if (d.ok) { loadAccts(); }
    else { alert(d.message || 'Failed to add account'); }
  } catch(e) { alert('Network error'); }
}

async function switchAccount(token) {
  await fetch('/api/accounts/switch', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({token: token})
  });
  loadAccts();
  document.getElementById('acct-drop').classList.remove('open');
}

async function removeAccount(token) {
  if (!confirm('Remove this account?')) return;
  await fetch('/api/accounts/remove', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({token: token})
  });
  loadAccts();
}
loadVersions();
checkGameStatus();
    loadAccts();
</script>
</body>
</html>
"""
