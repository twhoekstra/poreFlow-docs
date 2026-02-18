# On the stack

## Requirements

**Goal**: Reorganize nanopore data processing workflow and add GUIs for event filtering and annotation.

Must support the following features, ordered from features most commonly supported by frameworks/stacks to more specific features:

- Manage data
- Run processing algorithms (in Python/MATLAB)
- Plot data
- Select regions in plot (mark peptide/DNA regions in a POC read)
- Support hotkeys (for fast human data annotation)

## Options considered

### Dash & Plotly (Tested)

Recommended path for Python users who need interactive web-based visualization without deep knowledge of JavaScript/HTML. Pure-Python and very aesthetic. Locked-in to Plotly's ecosystem though, and limited support for hotkeys and data selection.

| Aspect | Description |
| :--- | :--- |
| **Focus** | Interactive, pure Python, browser-agnostic application. |
| **Core Technologies** | **Frontend/App Framework:** [Dash](https://dash.plotly.com/) (Built on Flask, React, and Plotly.js).<br>**Visualization:** [Plotly](https://plotly.com/python/) (Excellent interactivity, selection tools).<br>**Algorithm/Backend:** Pure Python.<br>**Async/Performance:** Use the `dask` library for parallel/out-of-core computations. |

Suitability for required features is listed below:

| Feature | Assessment |
| :--- | :--- |
| **Manage data** | **Good.** Files can be uploaded using Dash's `dcc.Upload` component (not tested). |
| **Run algorithms** | **Excellent.** Python algorithms run directly using Dash's callback system. Support for background threads/processes (not tested). |
| **Plot data** | **Best-in-Class.** Plotly is designed for scientific/financial data. It offers superior interactivity compared to Matplotlib. |
| **Select regions in a plot** | **Excellent.** Plotly supports built-in tools like lasso/box select, hover data, and zoom events, which can be captured. Does not support 1-D selection (e.g. based on just X selection). |
| **Hotkey support** | **Good.** Dash itself doesn't offer native hotkey support, but simple custom JavaScript added to app layout can be used instead. |

### Python & PyQt/PySide (Tested)

Pure desktop app. For a traditional, high-performance, native application experience that doesn't require a browser. This method was already used to create during a side-project for creating a GUI for

| Aspect | Description |
| :--- | :--- |
| **Focus** | High-performance, native look-and-feel, excellent hotkey integration. |
| **Core Technologies** | **GUI Framework:** [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) or PySide6 (Python bindings for the Qt framework).<br>**Visualization:** [Matplotlib](https://matplotlib.org/) (Embedded in a Qt widget via `FigureCanvasQtAgg`) or **PyQtGraph** (Specialized for fast, real-time scientific plotting).<br>**Algorithm/Backend:** Pure Python/NumPy/SciPy. |

### Suitability for Required Features

| Feature | Assessment |
| :--- | :--- |
| **Manage data** | **Excellent.** Native file dialogs provide great OS integration for loading and saving files. |
| **Run algorithms** | **Excellent.** Algorithms are run locally on the user's machine, often resulting in lower latency than web apps. Use Qt's thread system (`QThread`) for non-blocking execution. |
| **Plot data** | **Very Good.** Matplotlib offers publication-quality plots. PyQtGraph offers extremely fast interactive plotting, ideal for large datasets. |
| **Select regions in a plot** | **Excellent.** Both Matplotlib and PyQtGraph can be highly customized. You will implement direct event listeners (mouse clicks/drags) on the canvas to define regions. |
| **Hotkey support** | **Best-in-Class.** Native GUI frameworks like Qt offer powerful and straightforward mechanisms for global and context-specific keyboard shortcuts and menu bindings. |

### Project Structure (PyQt/PySide)

| Component | Description |
| :--- | :--- |
| `main_window.py` | Defines the main GUI layout, menus, toolbars, and integrates the different widgets (Plotting, Data Table, Controls). |
| `plotting_widget.py` | Custom widget that embeds the Matplotlib/PyQtGraph canvas and handles plot-specific interaction events (e.g., mouse drag for region selection). |
| `analysis_worker.py` | QThread sub-class used to run long-running algorithms in a separate thread, ensuring the GUI remains responsive. |
| `data_model.py` | Data structure (often subclassing `QAbstractTableModel`) to manage and expose data to the GUI components. |

---

### 3. Rapid Prototyping Web App: Python & Streamlit

For maximum speed of development and iteration, allowing you to focus almost entirely on the scientific code.

| Aspect | Description |
| :--- | :--- |
| **Focus** | Scientific focus, extreme simplicity, fast iteration (minimum boilerplate). |
| **Core Technologies** | **App Framework:** [Streamlit](https://streamlit.io/) (Turns Python scripts into interactive web apps).<br>**Visualization:** [Altair](https://altair-viz.github.io/) (Declarative, excellent interactivity) or **Plotly Express**.<br>**Algorithm/Backend:** Pure Python. |

### Suitability for Required Features

| Feature | Assessment |
| :--- | :--- |
| **Run Algorithms** | **Excellent.** Streamlit handles caching and re-running code efficiently. Perfect for quickly building prototypes of algorithms. |
| **Plot/Visualize Data** | **Very Good.** Altair and Plotly are natively supported and provide strong interactivity. |
| **Select Regions in a Plot** | **Good.** Altair excels at linked brushing and filtering |
