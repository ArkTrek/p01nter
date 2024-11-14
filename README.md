# p01nter 🎨
A simple yet powerful drawing application built with Python's `tkinter` library, enabling users to create and edit lines, curves, and other shapes. This application allows for dynamic drawing and modification of shapes, including changing line thickness, color, and background. It also includes features for saving and opening drawings in a custom format (`.ps` and `.json`), exporting the canvas as PNG images, and switching between light and dark modes.

## Features ✨

- **Draw Lines and Curves**: Draw and edit lines with adjustable points to create curves.
- **Change Line Thickness**: Dynamically adjust the thickness of your lines.
- **Color Customization**: Use color pickers to customize line and background colors.
- **Save and Open Drawings**: Save your work in `.ps` (PostScript) format and related `.json` data for future editing.
- **Export to PNG**: Export your artwork as a PNG image for sharing or printing.
- **Light/Dark Mode**: Toggle between light and dark modes. The app also supports Auto Mode, which switches themes based on the time of day (6 PM to 6 AM activates dark mode).
- **Undo and Redo**: Easily undo and redo actions using keyboard shortcuts (`Ctrl + Z` and `Ctrl + Y`).

## Installation 🔧

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/arktrek/p01inter.git
    cd paint-app
    ```

2. Install the required dependencies:
    ```bash
    pip install pillow
    ```

3. Run the `p01inter.py` script:
    ```bash
    python p01inter.py
    ```

## Usage 🖌️

- **Drawing**: Click and drag on the canvas to draw freehand lines.
- **Editing Lines**: Click and drag the control points on the lines to modify their shapes.
- **Adjust Line Thickness**: Use the slider in the toolbar to adjust the line thickness.
- **Line and Background Colors**: Use the color pickers in the toolbar to select line and background colors.
- **Saving and Opening Files**: Save your drawing as a `.ps` file and load it later. The `.json` file stores editable drawing data.
- **Exporting as PNG**: Save the current canvas as a PNG image using the export option in the file menu.
- **Undo and Redo**: Use `Ctrl + Z` for undo and `Ctrl + Y` for redo to manage your drawing history.
- **Theme Modes**: Toggle between **Light Mode**, **Dark Mode**, and **Auto Mode**. Auto Mode adjusts the theme based on the time of day (dark mode activates after 6 PM).


## Screenshots 📸

![Bg Changed](https://github.com/user-attachments/assets/be60ed9f-4b97-4f35-9a6e-77a9893280f2)

![Dark Mode](https://github.com/user-attachments/assets/dd9687ee-60e5-4216-af34-f3dbccb5a57a)

## Contributing 🤝

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

- The application uses the `tkinter` library for the GUI.
- `Pillow` library is used for image saving and manipulation.
- Thanks to the open-source community for their contributions to these libraries. ❤️

---

**Disclaimer: This is a work in progress and created for fun! Feel free to use it as a source of random inspiration and adapt it to your needs as you see fit.**
