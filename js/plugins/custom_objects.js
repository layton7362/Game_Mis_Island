function Window_Move_Sprite() {
    this.initialize.apply(this, arguments);
}

Window_Move_Sprite.prototype = Object.create(Window_Base.prototype);
Window_Move_Sprite.prototype.constructor = Window_Move_Sprite;

Window_Move_Sprite.prototype.initialize = function() {
    
    var width = this.windowWidth();
    var height = this.windowHeight();
    Window_Base.prototype.initialize.call(this, 0, 0, width, height);
    this.refresh();
};

Window_Move_Sprite.prototype.windowWidth = function() {
    return 240;
};

Window_Move_Sprite.prototype.windowHeight = function() {
    return this.fittingHeight(1);
};

Window_Move_Sprite.prototype.refresh = function() {
    // this.contents.clear();
    this.drawText("This game is Stupid",0,0,200)
};

