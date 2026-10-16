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

.red {
  --bg: #1a0000;
  --text: #ffffff;
  --placeholder: #a1a1a1;
  --button: rgba(25, 10, 10, 0.55);
  --button-border: rgba(255, 255, 255, 0.06);
  --icon: #a1a1aa;
  --toggle: #33C759;
  --slider: #0091FF;
  --element: rgba(36, 12, 12, 0.5);
  --element-border: rgba(255, 255, 255, 0.04);
  --card: rgba(36, 12, 12, 0.5);
  --card-border: rgba(255, 255, 255, 0.04);
  --overlay: rgba(0, 0, 0, 0.85);
  --input-bg: rgba(42, 14, 14, 0.55);
  --dropdown-bg: rgba(48, 16, 16, 0.65);
  --hover: rgba(255, 255, 255, 0.04);
  --hover-border: rgba(255, 255, 255, 0.08);
  --dropdown-item: rgba(255, 255, 255, 0.7);
  --dropdown-hover: rgba(255, 255, 255, 0.06);
  --focus-border: rgba(255, 255, 255, 0.15);
  --thumb: rgba(255, 255, 255, 0.06);
}
.red #titlebar {
  background: rgba(30, 0, 0, 0.48);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.blue {
  --bg: #00001a;
  --text: #ffffff;
  --placeholder: #a1a1a1;
  --button: rgba(0, 14, 36, 0.55);
  --button-border: rgba(255, 255, 255, 0.06);
  --icon: #a1a1aa;
  --toggle: #33C759;
  --slider: #0091FF;
  --element: rgba(0, 20, 55, 0.5);
  --element-border: rgba(255, 255, 255, 0.04);
  --card: rgba(0, 20, 55, 0.5);
  --card-border: rgba(255, 255, 255, 0.04);
  --overlay: rgba(0, 0, 0, 0.85);
  --input-bg: rgba(0, 24, 64, 0.55);
  --dropdown-bg: rgba(0, 28, 72, 0.65);
  --hover: rgba(255, 255, 255, 0.04);
  --hover-border: rgba(255, 255, 255, 0.08);
  --dropdown-item: rgba(255, 255, 255, 0.7);
  --dropdown-hover: rgba(255, 255, 255, 0.06);
  --focus-border: rgba(255, 255, 255, 0.15);
  --thumb: rgba(255, 255, 255, 0.06);
}
.blue #titlebar {
  background: rgba(0, 0, 42, 0.48);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
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
  user-select: none;
  -webkit-user-select: none;
  -webkit-user-drag: none;
  -moz-user-select: none;
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

.hero { display: flex; align-items: center; justify-content: center; gap: 16px; }
      .hero-center { margin: 0 auto; }
      .hero-right { min-width: 140px; }

.version-picker .dropdown-btn { min-width: 140px; padding: 12px 16px; font-size: 14px; }
.version-picker .dropdown-menu { min-width: 140px; }

.dl-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 10px;
  padding: 16px 44px; font-size: 16px; font-weight: 600;
  border: 1px solid var(--button-border); border-radius: 14px;
  cursor: pointer; background: var(--button); color: var(--text);
  font-family: inherit;
  backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
  transition: background 0.2s ease, border-color 0.2s ease, transform 0.15s ease;
}
.dl-btn:hover { background: var(--hover); border-color: var(--hover-border); }
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
.icon-btn svg { width: 22px; height: 22px; transition: transform 0.25s ease; }
.icon-btn.active { color: var(--text); }
.icon-btn.active svg { transform: rotate(90deg); }
      .icon-btn.open svg { transform: rotate(90deg); }
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
  visibility: hidden;
  overflow: hidden;
  transform: translateY(-6px);
  transition: max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.24s ease, transform 0.3s ease, visibility 0s linear 0.24s;
}
#settings-area.open {
  max-height: 70vh;
  opacity: 1;
  visibility: visible;
  overflow-y: auto;
  overflow-x: hidden;
  transform: translateY(0);
  transition: max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.24s ease, transform 0.3s ease, visibility 0s;
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
.c-slider-thumb { position: absolute; width: 36px; height: 22px; background: #fff; border-radius: 11px; box-shadow: 0 1px 4px rgba(0,0,0,0.3); top: 50%; margin-top: -11px; pointer-events: none; transition: left 0.18s ease-out; }

.dropdown { position: relative; }
.dropdown-btn {
  display: flex; align-items: center; justify-content: space-between; width: 100%; gap: 8px;
  padding: 12px 16px; background: var(--element);
  border: 1px solid var(--element-border); border-radius: 14px;
  color: var(--text); font-size: 14px; font-family: inherit;
  cursor: pointer; white-space: nowrap;
  transition: background 0.2s ease, border-color 0.2s ease;
}
.dropdown-btn:hover { background: var(--hover); border-color: var(--hover-border); }
.dropdown-btn:active { background: var(--hover); }
.dropdown-btn span { flex: 1; text-align: left; }
.dropdown-btn svg { width: 16px; height: 16px; margin-left: auto; opacity: 0.6; }
.dropdown-menu {
  position: absolute; top: calc(100% + 6px); left: auto; right: 0;
  min-width: 100%; background: var(--dropdown-bg);
  display: flex; flex-direction: column; gap: 1px;
  border: 1px solid var(--element-border); border-radius: 14px;
  padding: 4px; overflow: hidden; max-height: 50vh; z-index: 100;
  opacity: 0; visibility: hidden; transform: translateY(-6px) scale(0.96);
  pointer-events: none;
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  transition: opacity 0.2s ease, transform 0.2s ease, visibility 0s linear 0.2s;
}
.dropdown-menu.open { opacity: 1; visibility: visible; transform: translateY(0) scale(1); pointer-events: auto; overflow-y: auto; transition: opacity 0.2s ease, transform 0.2s ease, visibility 0s; }
.dropdown-item {
  padding: 10px 14px; font-size: 13px;
  color: var(--dropdown-item); cursor: pointer;
  border-radius: 10px;
  transition: background 0.15s ease, color 0.15s ease;
}
.dropdown-item:hover { background: var(--dropdown-hover); color: var(--text); }
.dropdown-item.selected { color: var(--slider); background: rgba(0,145,255,0.1); }
.dropdown-item.ver-old { color: #e6b800; }
.dropdown-item.ver-old::after { content: ' ⚠'; font-size: 11px; opacity: 0.85; }

.progress-bar { width: 100%; height: 4px; background: var(--card); border-radius: 3px; overflow: hidden; }
.progress-fill { height: 100%; background: var(--slider); border-radius: 3px; transition: width 0.4s ease; }

.config-group { display: flex; flex-direction: column; gap: 12px; width: 100%; }
.config-row { display: flex; flex-direction: column; gap: 6px; }
.config-label { font-size: 13px; font-weight: 600; color: var(--text); }
.config-input {
  padding: 10px 14px; background: var(--input-bg);
  border: 1px solid var(--hover-border); border-radius: 12px;
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
#save-btn:hover { background: var(--hover); }
#save-btn:active { background: #282828; }
#save-btn svg { width: 18px; height: 18px; }

#fixer-overlay {
  position: fixed; inset: 0; z-index: 9999;
  background: var(--overlay);
  display: none; align-items: center; justify-content: center;
}
#fixer-overlay.open { display: flex; }
.beta-warn { color: #fbbf24; font-size: 12px; margin-left: 4px; opacity: 0.95; }
.beta-toggles {
  border-top: 1px solid var(--element-border);
  padding: 10px 0 0 10px;
  max-height: 240px; opacity: 1; overflow: hidden;
  transition: max-height 0.18s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.14s ease,
              padding-top 0.18s cubic-bezier(0.4, 0, 0.2, 1), border-top-color 0.18s ease;
}
.beta-toggles.collapsed { max-height: 0; opacity: 0; padding-top: 0; border-top-color: transparent; }
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
  margin-left: 28px;
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

::-webkit-scrollbar { width: 0; height: 0; background: transparent; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: transparent; border-radius: 3px; }
html { scrollbar-width: none; }
.dropdown-menu::-webkit-scrollbar, #main::-webkit-scrollbar, #settings-area::-webkit-scrollbar { width: 0; height: 0; }
.dropdown-menu::-webkit-scrollbar-thumb, #main::-webkit-scrollbar-thumb, #settings-area::-webkit-scrollbar-thumb { background: transparent; }
.dropdown-menu, #main, #settings-area { scrollbar-width: none; scrollbar-color: transparent transparent; }

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
  opacity: 0; visibility: hidden; transform: translateY(-6px) scale(0.96);
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.2s ease, visibility 0s linear 0.2s;
}
.acct-drop.open { opacity: 1; visibility: visible; transform: translateY(0) scale(1); pointer-events: auto; transition: opacity 0.2s ease, transform 0.2s ease, visibility 0s; }
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

.mods-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  padding: 10px 28px; font-size: 13px; font-weight: 500;
  border: 1px solid var(--button-border); border-radius: 12px;
  cursor: pointer; background: var(--button); color: var(--text);
  font-family: inherit;
  backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
  transition: background 0.2s ease, border-color 0.2s ease, transform 0.15s ease;
}
.mods-btn:hover { background: var(--hover); border-color: var(--hover-border); }
.mods-btn:active { transform: scale(0.97); }

.cfg-btn {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 11px 24px; font-size: 14px; font-family: inherit;
  background: linear-gradient(rgba(255,255,255,0), rgba(255,255,255,0)), linear-gradient(var(--input-bg), var(--input-bg)), var(--input-bg);
  border: 1px solid var(--hover-border);
  border-radius: 999px; color: var(--text); cursor: pointer;
  transition: background 0.18s ease, border-color 0.18s ease;
}
.cfg-btn:hover {
  background: linear-gradient(var(--hover), var(--hover)), linear-gradient(var(--input-bg), var(--input-bg)), var(--input-bg);
  border-color: var(--focus-border);
}
.cfg-btn svg { width: 16px; height: 16px; }
.mods-btn svg { width: 22px; height: 22px; }
#mods-overlay {
  position: fixed; inset: 0; z-index: 9998;
  background: var(--overlay);
  display: none; align-items: center; justify-content: center;
}
#mods-overlay.open { display: flex; }
.mods-card {
  background: var(--card); border: 1px solid var(--card-border);
  border-radius: 20px; padding: 24px; max-width: 900px; max-height: 75vh;
  width: 90vw; display: flex; flex-direction: column;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
.mods-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-shrink: 0; }
.mods-title { font-size: 18px; font-weight: 600; }
.mods-close { background: none; border: none; color: var(--icon); cursor: pointer; padding: 6px; }
.mods-close:hover { color: var(--text); }
.mods-layout { display: flex; gap: 16px; flex: 1; min-height: 0; }
.mods-sidebar { min-width: 150px; flex-shrink: 0; overflow-y: auto; }
.mods-section-label { font-size: 11px; color: var(--placeholder); text-transform: uppercase; letter-spacing: 0.05em; margin: 14px 0 6px; }
.mods-filter { display: flex; flex-direction: column; gap: 4px; margin-bottom: 4px; }
.mods-filter-btn { padding: 7px 10px; font-size: 13px; border: 1px solid var(--element-border); border-radius: 10px; background: var(--element); color: var(--text); cursor: pointer; text-align: left; transition: background 0.15s; }
.mods-filter-btn:hover { background: var(--hover); }
.mods-filter-btn.active { color: var(--slider); background: rgba(0,145,255,0.1); border-color: var(--slider); }
.mods-list { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; min-height: 0; }
.mod-row {
  display: flex; align-items: center; gap: 12px; padding: 10px;
  border: 1px solid var(--element-border); border-radius: 14px; background: var(--element);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
}
.mod-row img { width: 64px; height: 64px; border-radius: 10px; object-fit: cover; flex-shrink: 0; background: var(--thumb); }
.mod-body { flex: 1; min-width: 0; }
.mod-name { font-size: 14px; font-weight: 500; }
.mod-desc { font-size: 12px; color: var(--placeholder); margin-top: 2px; }
.mod-cats { margin-top: 4px; display: flex; flex-wrap: wrap; gap: 4px; }
.mod-cat { font-size: 11px; color: var(--slider); background: rgba(0,145,255,0.1); padding: 2px 8px; border-radius: 6px; }
.mod-added { width: 18px; height: 18px; flex-shrink: 0; margin-top: 4px; stroke: var(--toggle); fill: none; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
.mod-add { flex-shrink: 0; padding: 8px 14px; font-size: 13px; border: 1px solid var(--element-border); border-radius: 10px; background: var(--button); color: var(--text); cursor: pointer; backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px); transition: background 0.2s; }
.mod-add:hover { background: var(--hover); }
.mod-remove { color: #ef4444; }
.mods-cta { margin: 16px auto 0; display: flex; justify-content: center; width: 100%; }
.mods-filter-btn { transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease, transform 0.15s ease; }
.mods-filter-btn:hover { transform: translateX(2px); }
.mods-filter-btn.active { transform: none; }
.mod-row { transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.15s ease; }
.mod-row:hover { transform: translateY(-1px); box-shadow: 0 4px 16px rgba(0,0,0,0.35); }
.mod-add { transition: background 0.15s ease, transform 0.15s ease; }
.mod-add:hover { transform: scale(1.05); }
.mods-card { opacity: 0; transform: translateY(8px); transition: opacity 0.18s ease, transform 0.18s ease; }
#mods-overlay.open .mods-card { opacity: 1; transform: translateY(0); }
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

#dlg-overlay {
  position: fixed; inset: 0; display: grid; place-items: center;
  padding: 16px; opacity: 0; visibility: hidden; pointer-events: none;
  background: var(--overlay); transition: opacity 0.2s ease, visibility 0s linear 0.2s; z-index: 10000;
}
#dlg-overlay.open { opacity: 1; visibility: visible; pointer-events: auto; transition: opacity 0.2s ease, visibility 0s; }
.dlg {
  position: relative; container-type: inline-size;
  width: min(480px, calc(100vw - 32px)); aspect-ratio: 1060 / 520;
  overflow: hidden; border-radius: 14.4% / 29.2%;
  background: linear-gradient(var(--card), var(--card)), var(--bg);
  box-shadow: 0 18px 46px rgba(0, 0, 0, 0.46); border: 1px solid var(--card-border);
}
.dlg-heading {
  position: absolute; top: 15.2%; left: 7.1%;
  display: flex; align-items: center; gap: 3.8cqw; white-space: nowrap;
}
.dlg-icon { display: block; flex: 0 0 6.52cqw; width: 6.52cqw; height: auto; overflow: visible; transform: translateY(-3px); }
.dlg-shape { fill: #ff383d; stroke: none; }
.dlg-mark { fill: none; stroke: #101010; stroke-width: 4.1; stroke-linecap: round; }
.dlg-mark-dot { fill: #101010; }
.dlg-title { margin: 0; color: var(--text); font-size: 5.6cqw; font-weight: 400; line-height: 1; letter-spacing: -0.025em; }
.dlg-desc {
  position: absolute; top: 37.2%; left: 6.3%; right: 6.3%; margin: 0;
  color: var(--placeholder); font-size: 4.72cqw; font-weight: 400; line-height: 1.22; letter-spacing: -0.012em;
}
.dlg-actions {
  position: absolute; right: 4.25%; bottom: 9.42%; left: 4.25%;
  display: grid; grid-template-columns: 1fr 1fr; gap: 2.9%; height: 27%;
}
.dlg-actions.single { grid-template-columns: 1fr; }
.dlg-btn {
  min-width: 0; padding: 0; position: relative; isolation: isolate;
  overflow: hidden; border-radius: 999px; font: inherit; font-size: 5.5cqw;
  font-weight: 400; line-height: 1; color: #f7f7f7; cursor: pointer;
  -webkit-tap-highlight-color: transparent; user-select: none;
  transition: background-color 0.18s ease, border-color 0.18s ease;
}
.dlg-btn-yes { border: 1px solid #ff383d; background: #ff383d; box-shadow: none; }
.dlg-btn-no { border: 1px solid #292929; background: #202020; box-shadow: none; }
.dlg-btn span { position: relative; z-index: 1; }
.dlg-btn:focus-visible { outline: 3px solid rgba(255, 255, 255, 0.85); outline-offset: 4px; }
.dlg-btn-yes:hover { background: #ff5257; border-color: #ff5257; }
.dlg-btn-no:hover { background: #2b2b2b; border-color: #333333; }
.dlg.info .dlg-shape { fill: #0091FF; }
.dlg.info .dlg-btn-yes { border-color: #0091FF; background: #0091FF; }
.dlg.info .dlg-btn-yes:hover { background: #2ba0ff; border-color: #2ba0ff; }
@media (max-width: 700px) {
  .dlg { width: min(480px, calc(100vw - 24px)); min-width: 0; border-radius: 10.8% / 18.5%; }
  .dlg-heading { top: 14%; left: 6.5%; gap: 2.8%; }
  .dlg-title { font-size: 5.2cqw; }
  .dlg-desc { top: 38%; left: 6.5%; right: 6.5%; font-size: 4.35cqw; letter-spacing: -0.025em; }
  .dlg-actions { right: 4%; bottom: 10%; left: 4%; gap: 2.5%; height: 26%; }
  .dlg-btn { font-size: 5cqw; }
}
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
    <a href="https://github.com/pileton/rigby-launcher" class="title-icon" onclick="openGithub();return false;" style="display:inline-flex;color:var(--icon);"><svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" stroke="none"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg></a>
  </div>

  <div id="main">
    <div id="center-wrap">
      <div class="hero">
        <div class="hero-left">
        <div class="dropdown version-picker" id="ver-dd">
          <div class="dropdown-btn" onclick="toggleDropdown('ver-dd')">
            <span id="ver-lbl">17.4I</span>
            <svg class="lucide" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
          </div>
          <div class="dropdown-menu" id="ver-menu"></div>
        </div>
        </div>
        <div class="hero-center">
        <button class="dl-btn" id="dl-main" onclick="handleDownload()">
          <svg class="lucide" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download
        </button>
        </div>
        <div class="hero-right">

        <button class="icon-btn" id="gear-btn" onclick="toggleSettings()">
          <svg class="lucide" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        </button>

        <button class="icon-btn" onclick="toggleChangelog()">
          <svg class="lucide" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
        </button>
        </div>
      </div>

      <div class="mods-cta">
        <button class="mods-btn" id="mods-btn" onclick="toggleMods()">
          <svg class="lucide" viewBox="0 0 24 24"><rect x="4" y="6" width="16" height="12" rx="2"/><path d="M8 6V4h8v4"/></svg>
          Mods
        </button>
      </div>

      <div class="element" id="dl-progress">
        <div class="element-info"><div class="element-title" id="dl-label">Downloading...</div></div>
        <div style="width:180px">
          <div class="progress-bar"><div class="progress-fill" id="dl-fill"></div></div>
          <div style="font-size:11px;color:var(--placeholder);margin-top:3px;text-align:right">
            <span id="dl-pct">0%</span><span id="dl-speed" style="margin-left:6px;opacity:0.85"></span>
          </div>
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
                  <div class="dropdown-item selected" data-val="dark" onclick="selectTheme('dark'); event.stopPropagation()">Dark</div>
                  <div class="dropdown-item" data-val="white" onclick="selectTheme('white'); event.stopPropagation()">White</div>
                  <div class="dropdown-item" data-val="red" onclick="selectTheme('red'); event.stopPropagation()">Red</div>
                  <div class="dropdown-item" data-val="blue" onclick="selectTheme('blue'); event.stopPropagation()">Blue</div>
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

            <div class="config-inline" style="border-top:1px solid var(--element-border);padding-top:12px">
              <div>
                <div style="font-size:14px;font-weight:500">⚠ BETA Resource watchdog</div>
                <div style="font-size:12px;color:var(--placeholder);margin-top:2px">⚠ BETA: monitor game/launcher resources; may terminate the game or lower launcher priority on sustained high usage</div>
              </div>
              <label class="toggle"><input type="checkbox" id="set-beta-watchdog" onchange="toggleBetaWatchdog()"><div class="toggle-track"></div></label>
            </div>
            <div class="beta-toggles collapsed" id="beta-toggles">
              <div class="config-inline" style="border-top:1px solid var(--element-border);padding-top:12px">
                <div>
                  <div style="font-size:14px;font-weight:500">Terminate game on high resources <strong style="color:#ef4444">⚠ BETA</strong></div>
                  <div style="font-size:12px;color:var(--placeholder);margin-top:2px">⚠ BETA: end the Among Us process when usage stays high</div>
                </div>
                <label class="toggle"><input type="checkbox" id="set-beta-terminate" onchange="toggleBetaTerminate(this)"><div class="toggle-track"></div></label>
              </div>
              <div class="config-inline" style="border-top:1px solid var(--element-border);padding-top:12px">
                <div>
                  <div style="font-size:14px;font-weight:500">Limit/launcher on high resources <strong style="color:#ef4444">⚠ BETA</strong></div>
                  <div style="font-size:12px;color:var(--placeholder);margin-top:2px">⚠ BETA: lower launcher priority when usage stays high</div>
                </div>
                <label class="toggle"><input type="checkbox" id="set-beta-limit" onchange="saveSettings()"><div class="toggle-track"></div></label>
              </div>
            </div>

            <div class="config-inline" style="border-top:1px solid var(--element-border);padding-top:12px">
              <div>
                <div style="font-size:14px;font-weight:500">Launcher Updates</div>
                <div style="font-size:12px;color:var(--placeholder);margin-top:2px">Reinstall or update Rigby Launcher itself</div>
              </div>
              <button class="cfg-btn" onclick="launcherUpdate()">
                <svg class="lucide" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="2" ry="2"/><path d="M7 12h10"/><path d="M12 7v10"/></svg>
                Update launcher
              </button>
            </div>

            <div class="element" style="border:none;border-radius: 4px ;padding:8px 0;background:transparent;margin-top:2px">
              <div class="element-info">
                <div class="element-desc" style="padding-left:6px">Launch delay (seconds)</div>
              </div>
              <div class="slider-wrap">
                <div class="c-slider" id="csl-delay" data-value="5">
                  <div class="c-slider-track"></div>
                  <div class="c-slider-fill" style="width:16.6%"></div>
                  <div class="c-slider-thumb" style="left:calc(16.6% - 18px)"></div>
                </div>
                <span class="slider-val" id="csl-delay-v" style="margin-left:-6px">5s</span>
              </div>
            </div>

            <div class="config-inline" style="border-top:1px solid var(--element-border);padding-top:12px">
              <div>
                <div style="font-size:14px;font-weight:500">Itch Login Fixer</div>
                <div style="font-size:12px;color:var(--placeholder);margin-top:2px">Authorize itch.io for game access</div>
              </div>
              <button class="cfg-btn" onclick="runFixer()">
                <svg class="lucide" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                Run Fixer
              </button>
            </div>


            <div class="config-row" style="border-top:1px solid var(--element-border);padding-top:12px">
              <div class="config-label">Game Directory</div>
              <div style="display:flex;gap:6px">
                <input class="config-input" type="text" id="set-game-dir" style="flex:1" placeholder="Select..." onblur="saveSettings()">
                <button class="icon-btn" onclick="openGameDir()" title="Open game folder" style="width:42px;height:42px;flex-shrink:0;border:1px solid var(--element-border);border-radius:50%">
                  <svg class="lucide" viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>
                </button>
              </div>
              <div id="game-dir-path" style="font-size:12px;color:var(--placeholder);margin-top:6px;word-break:break-all;cursor:default"></div>
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
      <div class="cl-ver">v0.7</div>
      <div class="cl-date">October 2026</div>
      <div class="cl-item">Fixed itch.io profile pictures not loading</div>
      <div class="cl-item">Game Directory now shows the correct folder and the button opens it</div>
      <div class="cl-item">Resource Watchdog options animate in and out instead of popping</div>
      <div class="cl-item">New pop up menu that replaces the native pop up (its cooler)</div>
    </div>
    <div class="cl-entry">
      <div class="cl-ver">v0.6</div>
      <div class="cl-date">September 2026</div>
      <div class="cl-item">Added AUnlocker v1.3.1 mod</div>
      <div class="cl-item">Settings gear now eases smoothly instead of snapping</div>
      <div class="cl-item">Changelog clock icon now spins open/close</div>
      <div class="cl-item">Balanced the hero row so version-picker / Play / gear never overlap on resize</div>
      <div class="cl-item">Mod icons now lazy-load and are cached to disk to cut image decode RAM</div>
    </div>
    <div class="cl-entry">
      <div class="cl-ver">v0.5</div>
      <div class="cl-date">August 2026</div>
      <div class="cl-item">Added blue theme</div>
      <div class="cl-item">Added red theme</div>
      <div class="cl-item">Added mod manager with BepInEx integration (direct .dll installs from GitHub)</div>
      <div class="cl-item">Fixed Hydra/Malum menu text not appearing (was a missing Wine corefonts; auto-installed on launch)</div>
      <div class="cl-item">In-launcher launcher reinstall/update</div>
      <div class="cl-item">Fixed spacing between dropdown options</div>
      <div class="cl-item">Nudged launch-delay slider labels</div>
      <div class="cl-item">New [BETA] Resource Watchdog</div>
      <div class="cl-item">Brightened red and blue themes for better contrast</div>
    </div>
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

<div id="mods-overlay">
  <div class="mods-card">
    <div class="mods-header">
      <div class="mods-title">Mods</div>
      <button class="mods-close" onclick="toggleMods()">&#10005;</button>
    </div>
    <div class="mods-layout">
      <div class="mods-sidebar">
        <div class="mods-section-label">Among Us versions</div>
        <div class="mods-filter" id="mods-versions"></div>
        <div class="mods-section-label">Categories</div>
        <div class="mods-filter" id="mods-categories"></div>
      </div>
      <div class="mods-list" id="mods-list"></div>
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

<div id="dlg-overlay">
  <div class="dlg" id="dlg" role="alertdialog" aria-labelledby="dlg-title" aria-describedby="dlg-desc">
    <div class="dlg-heading">
      <svg class="dlg-icon" viewBox="0 0 72 66" aria-hidden="true">
        <path class="dlg-shape" d="M27.1 5.8c4.1-6.9 13.7-6.9 17.8 0l25 42.6c3.8 6.5-.9 14.5-8.4 14.5H10.5c-7.5 0-12.2-8-8.4-14.5L27.1 5.8Z" />
        <path class="dlg-mark" d="M36 18.5v17.1" />
        <circle class="dlg-mark-dot" cx="36" cy="45.1" r="2.9" />
      </svg>
      <h1 class="dlg-title" id="dlg-title">Confirm ?</h1>
    </div>
    <p class="dlg-desc" id="dlg-desc">Are you sure?</p>
    <div class="dlg-actions" id="dlg-actions">
      <button class="dlg-btn dlg-btn-yes" type="button" id="dlg-yes" onclick="dialogYes()"><span>Yes</span></button>
      <button class="dlg-btn dlg-btn-no" type="button" id="dlg-no" onclick="dialogNo()"><span>No</span></button>
    </div>
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

const gradientWaveFragment = `precision highp float;
uniform vec3 uResolution;
uniform float uTime;
uniform vec2 uMouse;
uniform float uSpeed;
uniform float uAmplitude;
uniform float uWaveScale;
uniform float uWaveRatio;
uniform float uSwell;
uniform float uTurbulence;
uniform float uTilt;
uniform float uZoom;
uniform float uHeight;
uniform float uFogDepth;
uniform float uSteps;
uniform float uBrightness;
uniform float uOpacity;
uniform float uGrain;
uniform float uGrainIntensity;
uniform float uParallax;
uniform bool uEnableMouse;
uniform vec3 uHorizonColor;
uniform vec3 uWaveColor;
uniform vec3 uCrestColor;

const float MAX_DIST = 20000.0;

float hash21(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

float plasma(vec3 r, vec2 freq, vec4 tc) {
  float mx = r.x + tc.x;
  mx += uSwell * sin((r.y + mx) / 20.0 + tc.y);
  float my = r.y - tc.z;
  my += uTurbulence * cos(r.x / 23.0 + tc.w);
  return r.z - (sin(mx * freq.x) * uAmplitude + sin(my * freq.y) * uAmplitude + uHeight);
}

float raymarch(vec3 pos, vec3 dir, vec2 freq, vec4 tc) {
  float dist = 0.0;
  for (int i = 0; i < 128; i++) {
    if (float(i) >= uSteps) break;
    float dscene = plasma(pos + dist * dir, freq, tc);
    if (abs(dscene) < 0.1) break;
    dist += 0.9 * dscene;
    if (!(abs(dist) < MAX_DIST)) return MAX_DIST;
  }
  return dist;
}

void main() {
  float T = uTime * uSpeed;
  vec2 freq = vec2(uWaveScale / 7.0, (uWaveScale * uWaveRatio) / 3.0);
  vec4 tc = vec4(T / 0.130, T / 0.810, T / 0.200, T / 0.710);
  float c, s;
  float vfov = (3.14159 / 2.3) / max(uZoom, 0.05);
  vec3 cam = vec3(0.0, 0.0, 30.0);
  vec2 uv = (gl_FragCoord.xy / uResolution.xy) - 0.5;
  uv.x *= uResolution.x / uResolution.y;
  uv.y *= -1.0;

  vec3 dir = vec3(0.0, 0.0, -1.0);
  float ulen = length(uv);
  float xrot = vfov * ulen;
  c = cos(xrot); s = sin(xrot);
  dir = mat3(1.0, 0.0, 0.0, 0.0, c, -s, 0.0, s, c) * dir;
  vec2 nuv = ulen > 1e-5 ? uv / ulen : vec2(1.0, 0.0);
  c = nuv.x; s = nuv.y;
  dir = mat3(c, -s, 0.0, s, c, 0.0, 0.0, 0.0, 1.0) * dir;
  c = cos(uTilt); s = sin(uTilt);
  dir = mat3(c, 0.0, s, 0.0, 1.0, 0.0, -s, 0.0, c) * dir;

  if (uEnableMouse) {
    float yaw = (uMouse.x - 0.5) * uParallax * 0.4;
    float pitch = (uMouse.y - 0.5) * uParallax * 0.4;
    c = cos(yaw); s = sin(yaw);
    dir = mat3(c, 0.0, s, 0.0, 1.0, 0.0, -s, 0.0, c) * dir;
    c = cos(pitch); s = sin(pitch);
    dir = mat3(1.0, 0.0, 0.0, 0.0, c, -s, 0.0, s, c) * dir;
  }

  float dist = raymarch(cam, dir, freq, tc);
  vec3 pos = cam + dist * dir;

  float t = clamp(uFogDepth / max(dist, 0.001), 0.0, 1.0);
  vec3 body = mix(uWaveColor, uCrestColor, clamp(pos.z * 0.08 + 0.5, 0.0, 1.0));
  vec3 col = mix(uHorizonColor, body, t);
  col *= uBrightness;
  col = clamp(col, 0.0, 1.0);

  float alpha = clamp(t, 0.0, 1.0) * uOpacity;
  if (uGrain > 0.5) {
    float g = hash21(gl_FragCoord.xy + mod(uTime, 64.0) * 11.0);
    alpha += (g - 0.5) * uGrainIntensity;
  }
  alpha = clamp(alpha, 0.0, 1.0);
  gl_FragColor = vec4(col * alpha, alpha);
}`;

const THEME_COLORS = {
  dark: ['#5227FF', '#FF9EFC', '#FFFFFF'],
  white: ['#ffffff', '#FF9EFC', '#5227FF'],
  red: ['#450a0a', '#FF9EFC', '#FFFFFF'],
  blue: ['#011827', '#FF9EFC', '#FFFFFF']
};

const container = document.getElementById('waves');
const renderer = new Renderer({ alpha: true, premultipliedAlpha: false, webgl2: false });
const gl = renderer.gl;
gl.clearColor(0, 0, 0, 0);

let program;
let paused = false;
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

function uniformsFor(colors) {
  return {
    uTime: { value: 0 },
    uResolution: { value: [gl.canvas.width, gl.canvas.height, gl.canvas.width / gl.canvas.height] },
    uMouse: { value: new Float32Array([0.5, 0.5]) },
    uSpeed: { value: 0.4 }, uAmplitude: { value: 2.5 }, uWaveScale: { value: 0.6 },
    uWaveRatio: { value: 0.9 }, uSwell: { value: 35.0 }, uTurbulence: { value: 20.0 },
    uTilt: { value: 1.11 }, uZoom: { value: 1.0 }, uHeight: { value: 5.5 },
    uFogDepth: { value: 15.0 }, uSteps: { value: 70.0 }, uBrightness: { value: 1.0 },
    uOpacity: { value: 1.0 }, uGrain: { value: 1.0 }, uGrainIntensity: { value: 0.05 },
    uParallax: { value: 0.5 }, uEnableMouse: { value: true },
    uHorizonColor: { value: hexToVec3(colors[0]) }, uWaveColor: { value: hexToVec3(colors[1]) },
    uCrestColor: { value: hexToVec3(colors[2]) }
  };
}

program = new Program(gl, {
  vertex: vertexShader,
  fragment: gradientWaveFragment,
  uniforms: uniformsFor(THEME_COLORS.dark)
});

const mesh = new Mesh(gl, { geometry, program });
  gl.canvas.style.pointerEvents = 'none';
container.appendChild(gl.canvas);

gl.canvas.addEventListener('mousemove', handleMouseMove);
gl.canvas.addEventListener('mouseleave', handleMouseLeave);

let currentTheme = 'dark';

function syncColors(colors) {
  const u = program.uniforms;
  u.uHorizonColor.value = hexToVec3(colors[0]);
  u.uWaveColor.value = hexToVec3(colors[1]);
  u.uCrestColor.value = hexToVec3(colors[2]);
}

window.applyBackground = function(theme) {
  if (!gl) { setTimeout(function(){ window.applyBackground(theme); }, 100); return; }
  theme = (['dark', 'white', 'red', 'blue'].includes(theme)) ? theme : 'dark';
  syncColors(THEME_COLORS[theme] || THEME_COLORS.dark);
  const uRes = [gl.canvas.width, gl.canvas.height, gl.canvas.width / gl.canvas.height];
  if (program.uniforms.uResolution) program.uniforms.uResolution.value = uRes;
  renderer.render({ scene: mesh });
  currentTheme = theme;
  window.currentTheme = theme;
};
window.applyBackground('dark');

function update(time) {
  if (paused) return;
  requestAnimationFrame(update);
  program.uniforms.uTime.value = time * 0.001;

  currentMouse[0] += 0.05 * (targetMouse[0] - currentMouse[0]);
  currentMouse[1] += 0.05 * (targetMouse[1] - currentMouse[1]);
  program.uniforms.uMouse.value[0] = currentMouse[0];
  program.uniforms.uMouse.value[1] = currentMouse[1];
  renderer.render({ scene: mesh });
}

document.addEventListener('visibilitychange', function() {
  if (document.hidden) { paused = true; }
  else if (paused) { paused = false; requestAnimationFrame(update); }
});
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
let autoLaunchArmed = false;

function $(id) { return document.getElementById(id); }

let dialogState = { onConfirm: null, onDismiss: null };

function showDialog(opts) {
  opts = opts || {};
  $('dlg-title').textContent = opts.title || 'Confirm ?';
  $('dlg-desc').textContent = opts.desc || '';
  $('dlg-yes').querySelector('span').textContent = opts.yes || 'Yes';
  const noBtn = $('dlg-no');
  if (opts.no) {
    noBtn.style.display = '';
    noBtn.querySelector('span').textContent = opts.no;
    $('dlg-actions').classList.remove('single');
  } else {
    noBtn.style.display = 'none';
    $('dlg-actions').classList.add('single');
  }
  $('dlg').classList.toggle('info', opts.variant === 'info');
  const desc = $('dlg-desc');
  desc.style.fontSize = '';
  const actionsTop = $('dlg-actions').getBoundingClientRect().top;
  let fs = parseFloat(getComputedStyle(desc).fontSize) || 40;
  for (let i = 0; i < 8 && fs > 14 && desc.getBoundingClientRect().bottom > actionsTop - 6; i++) {
    fs *= 0.88;
    desc.style.fontSize = fs + 'px';
  }
  dialogState.onConfirm = opts.onConfirm || null;
  dialogState.onDismiss = opts.onDismiss || null;
  $('dlg-overlay').classList.add('open');
}

function hideDialog() { $('dlg-overlay').classList.remove('open'); }

function dialogYes() {
  const fn = dialogState.onConfirm;
  dialogState = { onConfirm: null, onDismiss: null };
  hideDialog();
  if (fn) fn();
}

function dialogNo() {
  const fn = dialogState.onDismiss;
  dialogState = { onConfirm: null, onDismiss: null };
  hideDialog();
  if (fn) fn();
}

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape' && $('dlg-overlay').classList.contains('open')) dialogNo();
});
$('dlg-overlay').addEventListener('click', function(e) {
  if (e.target === this) dialogNo();
});

function toggleSettings() {
  settingsOpen = !settingsOpen;
  $('settings-area').classList.toggle('open', settingsOpen);
  $('gear-btn').classList.toggle('active', settingsOpen);
  if (settingsOpen) { $('settings-area').scrollTop = 0; refreshStatus(); }
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
  const __ddEl = menu.querySelector('.dropdown-item[data-val="' + val + '"]'); if (__ddEl) __ddEl.classList.add('selected');
  menu.closest('.dropdown').querySelector('.dropdown-btn span').textContent = val;
  menu.classList.remove('open');
}

async function selectVer(val) {
  selectDD('ver-dd', val);
  try { await fetch('/api/versions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ version: val }) }); } catch (e) {}
}

function selectTheme(val) {
  selectDD('theme-dd', val);
  document.documentElement.classList.remove('white', 'red', 'blue');
  if (val === 'white') document.documentElement.classList.add('white');
  else if (val === 'red') document.documentElement.classList.add('red');
  else if (val === 'blue') document.documentElement.classList.add('blue');
  if (window.applyBackground && window.currentTheme !== val) window.applyBackground(val);
  saveSettings();
}

document.addEventListener('click', function(e) {
  if (e.target.closest('.dropdown-item')) return;
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
    thumb.style.left = 'calc(' + p + '% - 18px)';
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

function toggleChangelog() { var ov = $('cl-overlay'); ov.classList.toggle('open'); var b = document.querySelector('.icon-btn[onclick="toggleChangelog()"]'); if (b) b.classList.toggle('open', ov.classList.contains('open')); }
function openGithub() { window.location = 'https://github.com/pileton/rigby-launcher'; }

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
  loadAccts();
}

async function loadVersions() {
  try {
    const r = await fetch('/api/versions');
    const d = await r.json();
    const menu = $('ver-menu');
    menu.innerHTML = '';
    d.versions.forEach(v => {
      const item = document.createElement('div');
      const isOld = parseFloat(v) < 17;
      item.className = 'dropdown-item' + (v === d.selected ? ' selected' : '') + (isOld ? ' ver-old' : '');
      item.dataset.val = v;
      item.textContent = v;
      if (isOld) item.title = 'This version may not be supported by Innersloth.';
      item.onclick = function(e) { e.stopPropagation(); selectVer(v); };
      menu.appendChild(item);
    });
    $('ver-lbl').textContent = d.selected;
  } catch(e) {}
}

async function checkGameStatus() {
  try {
    const r = await fetch('/api/status');
    state = await r.json();
    if (state.settings?.theme) {
      document.documentElement.classList.remove('white', 'red', 'blue');
      if (state.settings.theme === 'white') document.documentElement.classList.add('white');
      else if (state.settings.theme === 'red') document.documentElement.classList.add('red');
      else if (state.settings.theme === 'blue') document.documentElement.classList.add('blue');
    }
    if (window.applyBackground && state.settings) {
      const _th = state.settings.theme || 'dark';
      if (window.currentTheme !== _th) window.applyBackground(_th);
    }
    if (state.latest_release && (state.versions || []).includes(state.latest_release) && state.latest_release !== state.installed_version) {
      $('update-badge').classList.add('show');
      if (state.settings?.auto_download && !downloading) {
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
    if (!verMatch || !state.game_installed) {
      autoLaunchArmed = false;
    }
    if (state.settings?.auto_launch && state.game_installed && !autoLaunchTimer && !autoLaunchArmed) {
      const delay = (state.settings.launch_delay || 5) * 1000;
      autoLaunchTimer = setTimeout(() => {
        autoLaunchTimer = null;
        autoLaunchArmed = true;
        if (!launching && state.wine_available) handlePlay();
      }, delay);
    }
  } catch(e) {}
  loadAccts();
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
    await handleDownload();
    checkGameStatus();
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
  try {
    const r = await fetch('/api/launch', { method: 'POST' });
    const d = await r.json();
    if (d.ok === false) {
      showDialog({ title: 'Launch Failed', desc: d.message || 'The game could not be launched.', yes: 'OK', variant: 'danger' });
    } else {
      checkGameStatus();
    }
  } catch(e) {}
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
        const spd = d.download_progress?.speed || 0;
        $('dl-speed').textContent = spd > 0 ? fmtSpeed(spd) : '';
        $('dl-label').textContent = d.download_progress?.extracting ? 'Extracting...' : 'Downloading…';
      } catch(e) {}
    }, 500);
  } catch(e) {}
}

async function refreshStatus() {
  try {
    const r = await fetch('/api/status');
    state = await r.json();
    const s = state.settings || {};
    const gd = state.game_dir || s.game_dir || '';
    $('set-game-dir').value = gd;
    $('set-wine-prefix').value = s.wine_prefix || '';
    $('set-wine-bin').value = s.wine_binary || 'wine';
    if ($('game-dir-path')) $('game-dir-path').textContent = gd ? (gd + '  •  ' + (state.game_installed ? 'Ready' : 'Not installed')) : 'No game directory detected';
    $('set-auto-update').checked = s.auto_download === true;
    $('set-auto-launch').checked = s.auto_launch === true;
    $('set-beta-watchdog').checked = s.beta_watchdog === true;
    if (s.beta_watchdog === true) {
      $('beta-toggles').classList.remove('collapsed');
      $('set-beta-terminate').checked = s.beta_terminate === true;
      $('set-beta-limit').checked = s.beta_limit_launcher === true;
    } else {
      $('beta-toggles').classList.add('collapsed');
    }
    const theme = s.theme || 'dark';
    $('theme-lbl').textContent = theme.charAt(0).toUpperCase() + theme.slice(1);
    const themeMenuItems = document.querySelectorAll('#theme-dd .dropdown-item');
    themeMenuItems.forEach(i => i.classList.toggle('selected', i.dataset.val === theme));
    document.documentElement.classList.remove('white', 'red', 'blue');
    if (theme === 'white') document.documentElement.classList.add('white');
    else if (theme === 'red') document.documentElement.classList.add('red');
    else if (theme === 'blue') document.documentElement.classList.add('blue');
    if (window.applyBackground && window.currentTheme !== theme) window.applyBackground(theme);
    const delay = s.launch_delay || 5;
    const dp = Math.round(delay / 30 * 100);
    const dsl = $('csl-delay');
    if (dsl) {
      dsl.dataset.value = dp;
      dsl.dataset.seconds = delay;
      dsl.querySelector('.c-slider-fill').style.width = dp + '%';
      dsl.querySelector('.c-slider-thumb').style.left = 'calc(' + dp + '% - 18px)';
      const ve = $('csl-delay-v');
      if (ve) ve.textContent = delay + 's';
    }
    if (!downloading) checkGameStatus();
    loadAccts();
  } catch(e) {}
}

async function openGameDir() {
  try {
    const r = await fetch('/api/open-folder', { method: 'POST' });
    const d = await r.json();
    if (!d.ok) showDialog({ title: 'Game Folder Not Found', desc: d.message || 'No game directory found yet — install the game first.', yes: 'OK', variant: 'danger' });
  } catch(e) {}
}

function fmtSpeed(bps) { if (!bps || bps <= 0) return ''; if (bps >= 1e6) return (bps / 1e6).toFixed(1) + ' MB/s'; if (bps >= 1e3) return (bps / 1e3).toFixed(1) + ' KB/s'; return bps + ' B/s'; }
function buildSettingsPayload() {
  return JSON.stringify({
    game_dir: $('set-game-dir').value,
    wine_prefix: $('set-wine-prefix').value,
    wine_binary: $('set-wine-bin').value,
    auto_download: $('set-auto-update').checked,
    auto_launch: $('set-auto-launch').checked,
    beta_watchdog: $('set-beta-watchdog').checked,
    beta_terminate: $('set-beta-terminate').checked,
    beta_limit_launcher: $('set-beta-limit').checked,
    theme: $('theme-lbl').textContent.trim().toLowerCase(),
    launch_delay: parseInt(($('csl-delay')?.dataset.seconds) || 5),
  });
}
async function flushPendingSettings() {
  const pending = localStorage.getItem('rigby-settings-pending');
  if (!pending) return;
  try { await fetch('/api/settings', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: pending }); } catch(e) {}
  try { localStorage.removeItem('rigby-settings-pending'); } catch(e) {}
  await new Promise(r => setTimeout(r, 120));
}

async function saveSettings() {
  const payload = buildSettingsPayload();
  try { localStorage.setItem('rigby-settings-pending', payload); } catch(e) {}
  if (navigator.sendBeacon) {
    const blob = new Blob([payload], { type: 'application/json' });
    if (navigator.sendBeacon('/api/settings', blob)) return;
  }
  try { await fetch('/api/settings', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: payload }); } catch(e) {}
}

function toggleBetaWatchdog() {
  const on = $('set-beta-watchdog').checked;
  $('beta-toggles').classList.toggle('collapsed', !on);
  if (!on) {
    $('set-beta-terminate').checked = false;
    $('set-beta-limit').checked = false;
  }
  saveSettings();
}

function toggleBetaTerminate(el) {
  if (!el.checked) { saveSettings(); return; }
  showDialog({
    title: 'Terminate Game ?',
    desc: 'The game will be closed when resource usage stays high. Progress may be lost.',
    yes: 'Enable', no: 'Cancel', variant: 'danger',
    onConfirm: function() { saveSettings(); },
    onDismiss: function() { el.checked = false; }
  });
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

var FROG_AVATAR = 'data:image/png;base64,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';

async function loadAccts() {
  try {
    var r = await fetch('/api/accounts');
    var d = await r.json();
    var list = document.getElementById('acct-list');
    list.innerHTML = '';
    var pillImg = document.getElementById('acct-pfp');
    pillImg.onerror = function() { this.onerror = null; this.src = FROG_AVATAR; };
    if (!pillImg.getAttribute('src')) { pillImg.src = FROG_AVATAR; }
    var pillName = document.getElementById('acct-name');
    var activeFound = false;
    d.accounts.forEach(function(acc) {
      var item = document.createElement('div');
      item.className = 'acct-item';
      if (acc.active) {
        item.classList.add('active');
        activeFound = true;
        pillImg.src = acc.avatar_url || FROG_AVATAR;
        pillImg.style.display = '';
        pillName.textContent = acc.username || 'Account';
      }
      var img = document.createElement('img');
      img.onerror = function() { this.onerror = null; this.src = FROG_AVATAR; };
      img.src = acc.avatar_url || FROG_AVATAR;
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
        item.onclick = function(e) { e.stopPropagation(); switchAccount(tok); };
      })(acc.token);
      list.appendChild(item);
    });
    if (!activeFound && d.accounts.length > 0) {
      pillImg.src = d.accounts[0].avatar_url || FROG_AVATAR;
      pillImg.style.display = '';
      pillName.textContent = d.accounts[0].username || 'Account';
    }
    if (!activeFound && d.accounts.length === 0) {
      pillImg.style.display = 'none';
      pillName.textContent = 'Account';
    }
    var addBtn = document.getElementById('acct-add-btn');
    addBtn.disabled = d.accounts.length >= d.max;
  } catch(e) {}
}

function launcherUpdate() {
  showDialog({
    title: 'Update Launcher ?',
    desc: 'The newest Rigby Launcher build will be downloaded and reinstalled.',
    yes: 'Update', no: 'Not now', variant: 'info',
    onConfirm: doLauncherUpdate
  });
}

async function doLauncherUpdate() {
  try {
    const r = await fetch('/api/launcher/update', { method: 'POST' });
    const d = await r.json();
    if (d.ok) {
      showFixerOverlay(d.message || 'Launcher updated', 'Restart the launcher to apply the update', true);
      setTimeout(hideFixerOverlay, 3500);
    } else {
      showDialog({ title: 'Update Failed', desc: d.message || 'Could not update the launcher.', yes: 'OK', variant: 'danger' });
    }
  } catch(e) {
    showDialog({ title: 'Update Failed', desc: 'Could not update the launcher.', yes: 'OK', variant: 'danger' });
  }
}

async function addAccount() {
  try {
    var r = await fetch('/api/accounts/add', { method: 'POST' });
    var d = await r.json();
    if (d.ok) { loadAccts(); }
    else { showDialog({ title: 'Add Account Failed', desc: d.message || 'The account could not be added.', yes: 'OK', variant: 'danger' }); }
  } catch(e) { showDialog({ title: 'Network Error', desc: 'Could not reach the launcher service.', yes: 'OK', variant: 'danger' }); }
}

async function switchAccount(token) {
  await fetch('/api/accounts/switch', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({token: token})
  });
  loadAccts();
  document.getElementById('acct-drop').classList.remove('open');
}

function removeAccount(token) {
  showDialog({
    title: 'Remove Account ?',
    desc: 'This account will be removed. This cannot be canceled.',
    yes: 'Remove', no: 'Cancel', variant: 'danger',
    onConfirm: async function () {
      try {
        await fetch('/api/accounts/remove', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({token: token})
        });
        loadAccts();
      } catch (e) {}
    }
  });
}

let modsState = {version: '', category: ''};
let modsCache = {versions: [], categories: [], mods: [], installed: [], bepinex_installed: false, current_version: ''};

function toggleMods() {
  const ov = $('mods-overlay');
  ov.classList.toggle('open');
  if (ov.classList.contains('open')) loadMods();
}

async function loadMods() {
  try {
    const r = await fetch('/api/mods');
    const d = await r.json();
    modsCache = d;
    if (!modsState.version) modsState.version = d.current_version || '';
    renderModFilters();
    renderMods();
  } catch(e) {}
}

function renderModFilters() {
  let vhtml = '<div class="mods-filter-btn" data-filter="version" data-val="">All versions</div>';
  (modsCache.versions || []).forEach(function(v) {
    vhtml += '<div class="mods-filter-btn" data-filter="version" data-val="' + v + '">' + v + '</div>';
  });
  $('mods-versions').innerHTML = vhtml;
  let ch = '<div class="mods-filter-btn" data-filter="category" data-val="">All categories</div>';
  (modsCache.categories || []).forEach(function(c) {
    ch += '<div class="mods-filter-btn" data-filter="category" data-val="' + c + '">' + c + '</div>';
  });
  $('mods-categories').innerHTML = ch;
  refreshModSelection();
}

function refreshModSelection() {
  document.querySelectorAll('.mods-filter-btn').forEach(function(b) {
    const isVer = b.dataset.filter === 'version';
    b.classList.toggle('active', isVer ? b.dataset.val === modsState.version : b.dataset.val === modsState.category);
  });
}

function setModFilter(field, val) {
  modsState[field] = val;
  refreshModSelection();
  renderMods();
}

document.addEventListener('click', function(e) {
  const b = e.target.closest('.mods-filter-btn');
  if (b) setModFilter(b.dataset.filter, b.dataset.val);
});

function renderMods() {
  const installed = modsCache.installed || [];
  const mods = (modsCache.mods || []).filter(function(m) {
    var mv = Array.isArray(m.version) ? m.version : (m.version ? [m.version] : []);
    if (modsState.version && !mv.includes(modsState.version)) return false;
    if (modsState.category && !(m.categories || []).includes(modsState.category)) return false;
    return true;
  });
  let html = '';
  if (!mods.length) {
    html = '<div style="color:var(--placeholder);padding:12px">No mods match these filters.</div>';
  }
  mods.forEach(function(m) {
    const isInstalled = installed.some(function(i) { return i.id === m.id; });
    let cats = (m.categories || []).map(function(c) { return '<span class="mod-cat">' + c + '</span>'; }).join('');
    html += '<div class="mod-row">';
    html += '<img src="' + m.image + '" alt="' + m.name + '" loading="lazy" width="40" height="40">';
    html += '<div class="mod-body">';
    html += '<div class="mod-name">' + m.name + '</div>';
    html += '<div class="mod-desc">' + m.description + '</div>';
    html += '<div class="mod-cats">' + cats + '</div>';
    html += isInstalled ? '<svg class="mod-added" viewBox="0 0 24 24"><polyline points="20 6 9 17 5 13"/></svg>' : '';
    html += '</div>';
    if (isInstalled) {
      html += '<button class="mod-add mod-remove" data-id="' + m.id + '" onclick="modRemove(this)" title="Remove mod">Remove</button>';
    } else {
      html += '<button class="mod-add" data-id="' + m.id + '" onclick="modInstall(this)" title="Add mod">Add</button>';
    }
    html += '</div>';
  });
  $('mods-list').innerHTML = html;
}

function modInstall(btn) {
  const id = btn.dataset.id;
  showDialog({
    title: 'Install Mod ?',
    desc: 'BepInEx will be set up automatically if it is missing.',
    yes: 'Install', no: 'Cancel', variant: 'info',
    onConfirm: async function () {
      try {
        const r = await fetch('/api/mods/install/' + id, { method: 'POST' });
        const d = await r.json();
        if (d.ok) {
          showDialog({ title: 'Mod Installed', desc: d.message || 'The mod was installed.', yes: 'OK', variant: 'info' });
          loadMods();
        } else {
          showDialog({ title: 'Install Failed', desc: d.message || 'The mod could not be installed.', yes: 'OK', variant: 'danger' });
        }
      } catch(e) { showDialog({ title: 'Install Failed', desc: 'The mod could not be installed.', yes: 'OK', variant: 'danger' }); }
    }
  });
}

function modRemove(btn) {
  const id = btn.dataset.id;
  showDialog({
    title: 'Remove Mod ?',
    desc: 'This mod will be removed from the game.',
    yes: 'Remove', no: 'Cancel', variant: 'danger',
    onConfirm: async function () {
      try {
        const r = await fetch('/api/mods/remove/' + id, { method: 'POST' });
        const d = await r.json();
        if (d.ok) {
          showDialog({ title: 'Mod Removed', desc: d.message || 'The mod was removed.', yes: 'OK', variant: 'info' });
          loadMods();
        } else {
          showDialog({ title: 'Remove Failed', desc: d.message || 'The mod could not be removed.', yes: 'OK', variant: 'danger' });
        }
      } catch(e) { showDialog({ title: 'Remove Failed', desc: 'The mod could not be removed.', yes: 'OK', variant: 'danger' }); }
    }
  });
}

loadVersions();
(async () => { await flushPendingSettings(); checkGameStatus(); })();
    loadAccts();
</script>
</body>
</html>
"""
