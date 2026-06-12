from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

def generate_image(prompt):

    image = pipe(
        prompt=prompt,
        guidance_scale=8.5,
        num_inference_steps=30
    ).images[0]

    return image 