import torch
from diffusers import StableDiffusionPipeline


# Function to initialize the model with the DDIM-Scheduler
def load_model():
    model_id = "stabilityai/stable-diffusion-2-1"  # Change this to your model ID
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Initialize the pipeline with float16 for better performance on compatible GPUs
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

    # Use the DPMSolverMultistepScheduler scheduler
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to(device)

    return pipe


# Global variable to store the loaded model
model = load_model()


# Function to generate an image from a prompt
# Function to generate an image from a prompt
def generate_image(prompt):
    with torch.no_grad():
        # Generate an image
        image = model(prompt).images[0]

    # Save the image
    image_path: str = r"C:\sample1\generated_image.png"  # Modify this path as needed
    image.save(image_path, format="PNG")

    return image_path



# Example usage
prompt = "a photo of an astronaut riding a horse on mars"
image_path = generate_image(prompt)
print(f"Image saved to {image_path}")
