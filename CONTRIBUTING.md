# Contributing to Network Science Air Transport Project

Thank you for your interest in contributing to this project!

## Development Workflow

### Setting Up Your Development Environment

1. Fork and clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/network-science-air-transport.git
cd network-science-air-transport
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Project Structure

- `src/` - Source code for network analysis modules
- `data/` - Data files (raw and processed)
- `notebooks/` - Jupyter notebooks for analysis
- `tests/` - Unit tests
- `docs/` - Documentation

## Adding New Features

### Task 1: Network Representation
Add implementations to `src/network_representation.py`:
- Data loading functions
- Graph creation utilities
- Network property calculations

### Task 2: Accessibility
Add implementations to `src/accessibility.py`:
- Centrality measures
- Shortest path analysis
- Accessibility indices

### Task 3: Community Detection
Add implementations to `src/community_detection.py`:
- Community detection algorithms
- Community analysis functions
- Visualization utilities

## Testing

Add unit tests in the `tests/` directory:
```bash
python -m unittest discover tests
```

## Code Style

- Follow PEP 8 guidelines
- Use descriptive variable and function names
- Add docstrings to all functions and classes
- Include type hints where appropriate

## Documentation

- Update README.md for major changes
- Add examples in Jupyter notebooks
- Update METHODOLOGY.md for new analysis approaches
- Document data formats in DATA_FORMAT.md

## Submitting Changes

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Description of your changes"
```

3. Push to your fork:
```bash
git push origin feature/your-feature-name
```

4. Open a Pull Request with:
   - Clear description of changes
   - Reference to related issues
   - Test results

## Questions?

If you have questions or need help, please open an issue on GitHub.
