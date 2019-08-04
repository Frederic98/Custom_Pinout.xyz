# Custom_Pinout.xyz
Run your own pinout.xyz server to manage your own custom made boards

Create a github repository with the directories `overlay` and `boards` to put the board definition and image.

Run the image with
```
docker run -d \
    -p 80:5000 \
    -e BOARDS_URL=https://github.com/Frederic98/Custom_Pinout.xyz.git \
    --name pinout \
    frederic98/custom_pinout.xyz
```
with BOARDS_URL pointing to your github repository
