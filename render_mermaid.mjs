// Render mermaid source (stdin) to an SVG string (stdout) at build time, so the
// built HTML needs no network. Needs Playwright; pass its node_modules folder
// in PLAYWRIGHT_NODE_MODULES if it is not resolvable from here.
import { createRequire } from "module";
import { readFileSync } from "fs";
const base = process.env.PLAYWRIGHT_NODE_MODULES || process.cwd() + "/node_modules";
const require = createRequire(base + "/");
const { chromium } = require("playwright");
const src = readFileSync(0, "utf8");
const browser = await chromium.launch();
const page = await browser.newPage();
await page.setContent(`<html><body><div id="out"></div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script></body></html>`, { waitUntil: "networkidle" });
const svg = await page.evaluate(async (code) => {
  mermaid.initialize({ startOnLoad: false, theme: "neutral", securityLevel: "loose", themeVariables: { fontSize: "13px" },
    flowchart: { htmlLabels: false, curve: "basis", nodeSpacing: 16, rankSpacing: 34, padding: 8, diagramPadding: 8 } });
  const { svg } = await mermaid.render("tree", code);
  return svg;
}, src);
await browser.close();
process.stdout.write(svg);
