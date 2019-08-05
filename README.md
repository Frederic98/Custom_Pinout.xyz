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

To keep the boards view uncluttered, the boards that are on [pinout.xyz](https://pinout.xyz) are removed, and only your own boards are displayed.

The board definitions are downloaded at every start of the container. So, after you updated your board(s), run `docker restart pinout` to reload them.
