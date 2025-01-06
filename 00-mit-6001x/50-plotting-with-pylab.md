# Plotting
We will be using the `pylab` library to plot our graphs/data.

## Plotting Plotting
`plot(x_values, y_values)` plots the data on the active figure.

- Assumes that both `x_values` and `y_values` are lists of the same length.

- The graph is displayed on a separate window where you can manipulate the graph if `plot()` is called from a regular python console.

- Otherwise, if it is called from an iPython console, it'll be embedded in the console but you'll lose the ability to play around with the graphs.

- You can also tell pylab what to name the plot by specifying an additional `label` argument (assumed to be a string). This name will be displayed in the legend if one is created.

```python
# Plot the given values with the name "some function".
pylab.plot(x_values, y_values, label="some function")
```

- If you want to change the color and the style of the plot, you can do that by providing an additional third argument (assumed to be a string).

  - The first part specifies the color of the plot, while the second part specifies the style.

```python
# "b" means blue and "-" means a solid line.
pylab.plot(x_values, y_values, "b-")

# "k" means black and "--" means a dashed line.
pylab.plot(x_values, y_values, "k--")

# There are many other options, such as "r" for red, "o" for circles, "^" for triangles, etc. Refer to the documentation if you wanna know more about the choices that you have.
```

- You can also specify the line width in a similar manner to `label` using the `line_width` parameter (assumed to be a float).

```python
pylab.plot(x_values, y_values, line_width=4.0)
```

## Multiple Figures
`figure(name)` tells pylab which figure or which window you want to do the processing on moving forward.

- Assumes that `name` is a string.

- This will create a new window if one does not exist for the figure with the given name.

```python
# "figure1" doesn't already exist so this makes a new window.
pylab.figure("figure1")

# plots the values on "figure1".
pylab.plot(x_values_1, y_values_1)

# "figure2" doesn't exist yet so this creates another new window.
pylab.figure("figure2")

# does both plottings on "figure2".
pylab.plot(x_values_2, y_values_2)
pylab.plot(x_values_3, y_values_3)
```

## Labels and Titles
`xlabel(text)` and `ylabel(text)` do exactly what their name suggests: show labels for the x-axis and the y-axis respectively.

- Assumes that `text` is a string.

```python
#... code from the "Multiple Figures" section

pylab.figure("figure1")  # "figure1" already exists so it is set as the active figure.
pylab.xlabel("samples")
pylab.ylabel("some function")

pylab.figure("figure2")  # sets "figure2" as active.
pylab.ylabel("some other function")
```

`title(text)` puts a title at the top of the graph.

- Assumes that `text` is a string.

```python
#... code from the previous example

pylab.title("Graph 2")  # displays the title for "figure2".
```

> **Dealing with residue from previous plotting operations**
> 
> If you continue plotting data with the functions we have discussed so far and frequently reuse old windows: at some point, you will run into a situation where the figures have some residue left over from previous plotting operations that were run on them (whether in form of old labels, old titles, anything) when you want to start with a clean slate.
>
> The `clf()` function, short for "clear frame", is used for this purpose. Running this wipes everything on the active figure/window and allows you to start anew.

> Get into the habit of clearing the frames when you reuse old windows or create new figures to ensure that you are starting with a blank canvas! Unless you don't want to clear the frame, of course.

## Legends
You can display a legend by calling the `legend()` function.

- You can also specify the location of the legend using the `loc` parameter!

```python
# Puts a legend in the upper left corner.
pylab.legend(loc="upper left")
```

## Axis Limits
The `xlim(min, max)` and `ylim(min, max)` functions allows us to set the range that the plot should display.

- Both assume that `min` and `max` are numbers.

```python
# Tells pylab to only display values associated with the samples between x=100 and x=500.
pylab.xlim(100, 500)
```

## Scales
The `xscale(scale)` and the `yscale(scale)` functions allow setting what scale should be used for the axes, e.g., linear, logarithmic, etc.

```python
# Sets the scale on the y-axis to 'logarithmic'.
pylab.yscale("log")
```

## Subplots
`subplot(n_rows, n_columns, position)` allows us to layout our plots in a figure by creating grid-like sub-divisions.

- Assumes that `n_rows`, `n_columns`, and `position` are all ints.

- It basically works like figure but for the desired division/layout, i.e., it treats the different divisions like they are a frame of their own and any successive operations will be done on the active frame (or division in this case).

```python
# "Divides" the active figure into 1 row and 2 columns, and then sets the first out of those divisions as the active frame.
pylab.subplot(1, 2, 1)
```
