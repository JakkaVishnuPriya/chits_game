# ChitJar — The Lucky Draw Experience

A personal Streamlit-hosted random chit picker with a glass-bowl interface, colourful paper chits, animated mixing/picking/unfolding, generated sound effects, Excel/CSV/TXT import, event history, and browser-side event storage.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository and upload **all files and folders** from this project (keep `app.py`, `chitjar.html`, `requirements.txt`, and `.streamlit/config.toml` in the repository root / indicated paths).
2. In Streamlit Community Cloud choose **New app**, select the repository and branch, and set the main file path to `app.py`.
3. Deploy. No API key or database credentials are required.

## Data storage and privacy

Events are stored in the browser's IndexedDB database on the device/browser where the app is used. The lists and results are not sent to a server database. This is convenient for a personal picker and survives normal browser restarts, but it does **not** automatically sync across devices or browsers. Clearing browser site data can erase the saved events, so use **Download database backup** periodically and restore it when needed. Excel import uses the SheetJS browser library from jsDelivr; internet access is needed for that library to load.

## Included behavior

- One entry per line; supports large lists and no fixed input-count cap.
- XLSX/XLS, CSV and TXT imports (first worksheet / first CSV column).
- Draw one or multiple chits; default is without replacement.
- Exclude picked chits, allow replacement, or automatically begin another round when exhausted.
- Return a picked chit to the bowl or keep it out.
- Each saved event stores its own list, settings, picked list, and ordered draw history.
- CSV result export and JSON database backup/restore.
- Full-screen jar mode, animated bowl mixing, paper selection and unfolding.
- Sound effects are synthesized in the browser; sound starts after a user gesture and can be muted/adjusted.

## Notes

The interface is an original implementation inspired by the interaction pattern of Random Jar, not a copy of its source code or branding. Browser fullscreen support depends on the browser and whether it permits fullscreen from the embedded app frame.
