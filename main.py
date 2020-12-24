sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    Santa.setPosition(randint(0, 80), randint(0, 80))
    info.startCountdown(5)
})
let Santa: Sprite = null
game.splash("Chase Santa Claus (v1.0)")
scene.setBackgroundColor(9)
let John = sprites.create(img`
    a e 3 . a 7 e c a e 
    `, SpriteKind.Player)
controller.moveSprite(John)
Santa = sprites.create(img`
    a e 3 . a 7 e a 5 3 a 
    `, SpriteKind.Food)
info.startCountdown(5)
