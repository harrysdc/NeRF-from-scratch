Implement an implicit volume as a Multi-Layer Perceptron (MLP) in the `NeuraRadianceField` class in `implicit.py`. This MLP should map 3D position to volume density and color. Specifically:

1. Your MLP should take in a `RayBundle` object in its forward method, and produce color and density for each sample point in the RayBundle.
2. You should also fill out the loss in `train_nerf` in the `main.py` file.

## Implementation.
1. You should use the `ReLU` activation to map the first network output to density (to ensure that density is non-negative)
2. You should use the `Sigmoid` activation to map the remaining raw network outputs to color
3. You can use *Positional Encoding* of the input to the network to achieve higher quality. We provide an implementation of positional encoding in the `HarmonicEmbedding` class in `implicit.py`.

## Visualization
![Spiral Rendering of Part 3](ta_images/part_3.gif)
