#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = "https://swapi-api.hbtn.io/api/films/" + movieId + "/";

function fetchCharacterNames(characters, index) {
    if (index >= characters.length) {
        return;
    }

request(characters[index], function(error, response, body) {
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    fetchCharacterNames(characters, index + 1);
});
}

request(url, function(error, response, body) {
    if (error) {
        console.error('Error:', error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error('Failed to fetch data. Status code:', response.statusCode);
        return;
    }

    try {
        const data = JSON.parse(body);
        const characters = data.characters;

        fetchCharacterNames(characters, 0);
    } catch (parseError) {
        console.error('Error parsing film data:', parseError);
    }
});
