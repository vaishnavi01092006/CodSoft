print("======================================")
print("       IMAGE CAPTIONING SYSTEM")
print("======================================")
captions = {
    "dog.jpg": "A dog is playing in the park.",
    "cat.jpg": "A cute cat is sleeping on the sofa.",
    "car.jpg": "A red car is parked on the road.",
    "flower.jpg": "Beautiful flowers are blooming in the garden.",
    "bird.jpg": "A bird is sitting on a tree branch."
}
print("\nAvailable Images:")
for image in captions:
    print("-", image)
image_name = input("\nEnter image name: ")
if image_name in captions:
    print("\nGenerated Caption:")
    print(captions[image_name])
else:
    print("\nImage not found.")