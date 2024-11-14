# p01nter
A simple yet powerful drawing application built with Python's `tkinter` library, enabling users to create and edit lines, curves, and other shapes. This application allows for dynamic drawing and modification of shapes, including changing line thickness, color, and background. It also includes features for saving and opening drawings in a custom format (`.ps` and `.json`), exporting the canvas as PNG images, and switching between light and dark modes.

## Features

- **Draw Lines and Curves**: Users can draw and edit lines, with the ability to manipulate points along the line to create curves.
- **Change Line Thickness**: Modify the thickness of drawn lines dynamically.
- **Color Customization**: Use color pickers to choose line colors and background color.
- **Save and Open Drawings**: Save the drawing as `.ps` (PostScript) files and related JSON data for future editing.
- **Export to PNG**: Export the canvas as a PNG image.
- **Light/Dark Mode**: Switch between light and dark themes manually or automatically based on the time of day (6 PM to 6 AM defaults to dark mode).
- **Undo and Redo**: Keyboard shortcuts (`Ctrl + Z` for undo, `Ctrl + Y` for redo) for easy editing.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/paint-app.git
    cd paint-app
    ```

2. Install the required dependencies:
    ```bash
    pip install pillow
    ```

3. Run the `paint_app.py` script:
    ```bash
    python paint_app.py
    ```

## Usage

- **Drawing**: Click and drag on the canvas to draw lines.
- **Editing Lines**: Click and drag the control points of a line to modify its shape.
- **Line Thickness**: Use the slider in the toolbar to adjust the thickness of the lines.
- **Line and Background Colors**: Use the color pickers in the toolbar to select the colors for lines and the background.
- **Saving and Opening Files**: You can save your drawing as a `.ps` file and load it later. The `.json` file stores editable drawing data.
- **Exporting as PNG**: Save the current canvas as a PNG image using the export option in the file menu.
- **Undo and Redo**: Use `Ctrl + Z` for undo and `Ctrl + Y` for redo to manage your drawing history.
- **Theme Modes**: Toggle between Light Mode, Dark Mode, and Auto Mode. Auto Mode changes the theme based on the time of day (dark mode activates after 6 PM).

## Screenshots

![Bg Changed](https://github.com/user-attachments/assets/be60ed9f-4b97-4f35-9a6e-77a9893280f2)

![Dark Mode](https://github.com/user-attachments/assets/dd9687ee-60e5-4216-af34-f3dbccb5a57a)


## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The application uses the `tkinter` library for creating the GUI.
- `Pillow` library is used for handling image saving and manipulation.
- Thanks to the open-source community for their contributions to these libraries.
