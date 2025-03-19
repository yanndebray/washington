
# Data Analysis and AI demo
```matlab
weatherData = generateSyntheticWeatherData(100)
```


| |Temperature|Humidity|WindSpeed|Label|
|:--:|:--:|:--:|:--:|:--:|
|1|33|16|13|1|
|2|37|80|7|3|
|3|5|31|17|3|
|4|37|53|11|3|
|5|25|16|7|3|
|6|3|60|19|3|
|7|11|26|18|3|
|8|22|66|11|3|
|9|39|69|13|3|
|10|39|75|12|3|
|11|6|45|4|3|
|12|39|8|6|1|
|13|39|23|9|1|
|14|19|92|4|3|


# Utilities
```matlab
function weatherData = generateSyntheticWeatherData(numSamples)
    % Generate synthetic weather dataset for classification
    % Inputs:
    %   numSamples - Number of samples to generate
    % Outputs:
    %   weatherData - A table containing synthetic weather data

    % Set random seed for reproducibility
    rng(0);

    % Generate synthetic features
    temperature = randi([0, 40], numSamples, 1); % Temperature in degrees Celsius
    humidity = randi([0, 100], numSamples, 1); % Humidity in percentage
    windSpeed = randi([0, 20], numSamples, 1); % Wind speed in km/h

    % Generate synthetic labels based on conditions
    labels = zeros(numSamples, 1);
    for i = 1:numSamples
        if temperature(i) > 30 && humidity(i) < 50
            labels(i) = 1; % Class 1: Hot and dry
        elseif temperature(i) < 10 && humidity(i) > 80
            labels(i) = 2; % Class 2: Cold and wet
        else
            labels(i) = 3; % Class 3: Mild
        end
    end

    % Create a table to hold the data
    weatherData = table(temperature, humidity, windSpeed, labels, ...
        'VariableNames', {'Temperature', 'Humidity', 'WindSpeed', 'Label'});
end
```
