sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    Santa.setPosition(randint(0, 80), randint(0, 80))
    info.startCountdown(5)
})
let Santa: Sprite = null
game.splash("Chase Santa Claus (v1.0)")
scene.setBackgroundColor(9)
let John = sprites.create(assets.image`player`, SpriteKind.Player)
controller.moveSprite(John)
Santa = sprites.create(assets.image`Santa`, SpriteKind.Food)
info.startCountdown(5)
