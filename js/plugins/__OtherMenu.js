(function() {

    var _Scene_Menu_create = Scene_Menu.prototype.create;
    Scene_Menu.prototype.create = function() {
        _Scene_Menu_create.call(this);
        this._statusWindow.x = 0;
        this._statusWindow.y = this._commandWindow.height;
        this._goldWindow.x = Graphics.boxWidth - this._goldWindow.width;
    };

    Window_MenuCommand.prototype.windowWidth = function() {
        return Graphics.boxWidth;
    };

    Window_MenuCommand.prototype.maxCols = function() {
        return 4;
    };

    Window_MenuCommand.prototype.numVisibleRows = function() {
        return 2;
    };

    Window_MenuStatus.prototype.windowWidth = function() {
        return Graphics.boxWidth;
    };

    Window_MenuStatus.prototype.windowHeight = function() {
        var h1 = this.fittingHeight(1);
        var h2 = this.fittingHeight(2);
        return Graphics.boxHeight - h1 - h2;
    };

    Window_MenuStatus.prototype.maxCols = function() {
        return 4;
    };

    Window_MenuStatus.prototype.numVisibleRows = function() {
        return 1;
    };

    Window_MenuStatus.prototype.drawItemImage = function(index) {
        // No Face 
    };

    Window_MenuStatus.prototype.itemRectForText = function(index) {
        var rect = this.itemRect(index);
        rect.x += this.textPadding();
        rect.width -= this.textPadding();
        return rect;
    };
    
    Window_MenuStatus.prototype.drawItemBackground = function(index) {
        // Do nothing
    };

    Window_MenuStatus.prototype.itemRect = function(index) {
        const PADDING = 30
        var rect = new Rectangle();
        var maxCols = this.maxCols();
        rect.width = this.itemWidth(); 
        rect.height = 150;
        rect.x = index % maxCols * (rect.width + this.spacing()) - this._scrollX;
        rect.y = Math.floor(index / maxCols) * rect.height - this._scrollY;
        return rect;
    };

    Window_MenuStatus.prototype.drawItemStatus = function(index) {
        var actor = $gameParty.members()[index];
        var rect = this.itemRectForText(index);
        var x = rect.x;
        var y = rect.y;
        var width = rect.width;
        var bottom = y + rect.height;
        var lineHeight = this.lineHeight();
        // this.drawActorName(actor, x, y + lineHeight * 0, width);
        // this.drawActorLevelNumber(actor, x, y + lineHeight * 1, width);
        // this.drawActorClass(actor, x, bottom - lineHeight * 4, width);
        this.drawActorName(actor, x, bottom - lineHeight * 4);
        this.drawActorHp(actor, x, bottom - lineHeight * 3, width);
        this.drawActorMp(actor, x, bottom - lineHeight * 2, width);
        this.drawActorIcons(actor, x, bottom - lineHeight * 1, width);
    };

    var _Window_MenuActor_initialize = Window_MenuActor.prototype.initialize;
    Window_MenuActor.prototype.initialize = function() {
        _Window_MenuActor_initialize.call(this);
        this.y = this.fittingHeight(2);
    };

})();
