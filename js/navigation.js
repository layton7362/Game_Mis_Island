// World Navigation Logic

class NavMapData {
    constructor(_map_id, name) {
        this.map_id = _map_id
        this.name = name
    }

}

function Navigation(){
    throw new Error('This is a static class');
}

Navigation.initialize = function(){

    this.initMember.call(this)
}

Navigation.initMember = function(){

    this.map_height = 17;
    this.map_width = 13;
    this.area_count_x = 26 
    this.area_count_y = 'Z'.charCodeAt(0) - 'A'.charCodeAt(0) + 1

    var map_id = 0 // add with +4, because the MapId Begins with 4
    this._map = new Array(this.area_count_y);
    var letter = 'A'.charCodeAt(0) - 1
    for (var y = 0; y < this.area_count_y; y++) 
    {   
        map_id += 1
        letter += 1
        this._map[y] = new Array(this.area_count_x);
        for (var x = 0; x < this.area_count_x; x++){
            var name = String.fromCharCode(letter) + x
            this._map[x][y] = new NavMapData(map_id + 4, name)
            map_id += 1
        }
    }
};

Navigation.get = function(x,y){
    return this._map[x][y]
}

Navigation.initialize()


