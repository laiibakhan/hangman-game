from PIL import Image
import os

# Process letter images
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in letters:
    img_path = f'{letter}.png'
    if os.path.exists(img_path):
        try:
            # Open image
            img = Image.open(img_path)
            
            # Convert to RGBA if not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Get image data
            data = img.getdata()
            
            # Remove white or light backgrounds
            new_data = []
            for item in data:
                # If pixel is white or very light, make it transparent
                if item[0] > 240 and item[1] > 240 and item[2] > 240:
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)
            
            img.putdata(new_data)
            
            # Resize to smaller size (40x40)
            img = img.resize((40, 40), Image.Resampling.LANCZOS)
            
            # Save with transparency
            img.save(img_path)
            print(f"Processed: {letter}.png")
        except Exception as e:
            print(f"Error processing {letter}.png: {e}")

print("Image processing complete!")
