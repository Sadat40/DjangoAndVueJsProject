<template>
    <a :href="this.game_list_url">Games list</a><br/>
    <a :href="this.game_update_url">Update Game</a><br/>
    <a :href="this.game_delete_url">Delete Game</a><br/>
    <h1>{{ this.game.name }}</h1>
    Characters:<br/>
    <span v-for="character in this.game.characters">
    {{character.name}}<br/></span>
    <br/>
    Running time: {{this.convert_time_to_string(this.game.running_time)}}<br/>
    Director: {{this.game.director}}<br/>
    Release date: {{this.convert_date_to_string(this.game.release_date)}}<br/>
    </template>
    
    <script>
    
    export default {
      name: 'App',
      components: {
      },
      data: function() {
          return {
            game_error: [],
            game_id: ext_game_id,
            game_detail_js_url: ext_game_detail_js_url,
            game_list_url: ext_game_list_url,
            game_update_url: ext_game_update_url,
            game_delete_url: ext_game_delete_url,
            game: {}
        }},
        methods: {
            get_game_info(){
                fetch(this.game_detail_js_url,
                    {
                        method: "get",
                        credentials: 'same-origin'
                    }
                ).then(function(response) {
                    console.log('response', response)
                    return response.json()}).then(this.assign_game).catch(
                        (error) => { 
                        console.log('error', error)
                        this.game_error=["error when loading game information"]
            })
            },
            assign_game(game_json) {
                console.log('json', game_json)
                this.game = game_json['game']
                this.game.running_time = this.convert_string_to_time(
                    this.game.running_time)
                this.game.release_date = this.init_date(
                    this.game.release_date
                )
            },
            convert_string_to_time(time_string) {
                return new Date("1970-01-01T" + time_string)
            },
            init_date(date_string){
                let dato = new Date(date_string)
                const offset = dato.getTimezoneOffset()
                dato = new Date(dato.getTime() + (offset*60*1000))
                return dato
            },
            convert_date_to_string(dato){
                if (dato) {
                    const offset = dato.getTimezoneOffset()
                    dato = new Date(dato.getTime() - (offset*60*1000))
                    console.log('date', dato, dato.toISOString())
                    return dato.toISOString().split('T')[0]
                }
            },
            convert_time_to_string(timo){
                if (timo) {
                    return `${timo.getHours()} hours ${timo.getMinutes()} minutes`
                }
            }
        },
        computed: {
        },
        beforeMount() {
            this.get_game_info()
        },
    }
    </script>