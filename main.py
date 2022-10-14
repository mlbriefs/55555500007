import os
import imageio
import numpy as np

# if you need to access a file next to the source code, use the variable ROOT
# for example:
#    torch.load(os.path.join(ROOT, 'weights.pth'))
ROOT = os.path.dirname(os.path.realpath(__file__))

def main(input, output, sigma):
    u = imageio.read(input)
    print("hello world", u.shape)

    v = u + np.random.randn(*u.shape) * sigma

    imageio.ims(output, v)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, required=True)
    parser.add_argument("--sigma", type=float, required=True)

    args = parser.parse_args()
    noisy_1 = main(args.input, args.sigma)
    noisy_2 = main(args.input, 2*args.sigma)
    imageio.imwrite("output_0.png", noisy_1)
    imageio.imwrite("output_1.png", noisy_2)
