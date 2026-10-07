<!-- HEADER START -->
<p align="center">
  <img src="https://shields.io" alt="Version">
  <img src="https://shields.io" alt="Category">
  <img src="https://shields.io" alt="Language">
</p>

<h1 align="center">🧶 LoomSec</h1>

<p align="center">
  <strong>LoomSec</strong> is a lightweight, linear, and high-speed <strong>Software Composition Analysis (SCA)</strong> tool designed to scan project dependencies for known vulnerabilities using the Google OSV API.
</p>
<!-- HEADER END -->

<hr />

## 🚀 Features
* **Zero Overhead:** No heavy setup or massive local databases required.
* **Real-time Threat Intelligence:** Queries the **Google OSV (Open Source Vulnerabilities)** database instantly.
* **Beautiful Reporting:** Built-in UI leveraging `rich` for clean, colored terminal tables.
* **Ecosystem Support:** Currently tracking **PyPI** (`requirements.txt`) with an extensible architecture.

## 🛠️ Installation & Usage

### 1. Clone & Install Dependencies
```bash
pip install requests rich
```

### 2. Execution
```bash
python loomsec.py
```

<hr />

## 📊 Technical Architecture

LoomSec operates on a straightforward, linear pipeline to ensure rapid execution without code bloat:

<pre>
[User Input] ➔ [Parse requirements.txt] ➔ [Extract SemVer] ➔ [Google OSV API Query] ➔ [Rich Terminal UI]
</pre>

<hr />

## 📜 License & Author
* Developed by **4B2A**
* Version: `1.0.0`
* Intended for security researchers, developers, and AppSec engineers.
