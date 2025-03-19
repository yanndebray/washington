Yann:
call astropy from MATLAB

Copilot:
To call the Astropy library from MATLAB, you can utilize the built-in functionality to call Python libraries directly. Here's a concise example demonstrating how to do this:

1. **Ensure Python and Astropy are installed** on your system and that MATLAB is configured to use the correct Python version.

2. **Use the following MATLAB code** to call a function from Astropy. For example, let's use Astropy's `Time` class to convert a time string to a time object:

```matlab
% Check if Python is configured correctly
pyversion

% Import the Astropy Time module
astropy_time = py.importlib.import_module('astropy.time');

% Create a Time object from a string
time_str = '2023-10-01T12:00:00';
time_obj = astropy_time.Time(time_str);

% Display the Time object
disp(time_obj)
```

### Explanation:
- `py.importlib.import_module('astropy.time')` imports the Astropy Time module.
- `astropy_time.Time(time_str)` creates a Time object from the specified string.
- The result is displayed in MATLAB.

Make sure to replace `time_str` with any valid time string you wish to convert. This approach allows you to leverage the capabilities of Astropy directly within your MATLAB environment.

