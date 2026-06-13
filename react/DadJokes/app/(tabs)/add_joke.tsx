// File: add_joke.tsx
// Author: Emily Vespasiano (evespa@bu.edu), 6/13/2026
// Description: The Add Joke screen tab which allows users to create a new joke.
import { Text, View, TouchableOpacity, TextInput } from 'react-native';
import { styles } from '../../assets/my_styles';
import { useState } from 'react';

export default function AddJokeScreen() {

     // tracks the joke text, posting state, and author name
    const [jokeText, setJokeText] = useState('');
    const [isPosting, setIsPosting] = useState(false);
    const [author, setAuthor] = useState('');

    const addJoke = async () => {
        // posts new joke to the API
        setIsPosting(true)
        try {
          const response = await fetch('https://cs-webapps.bu.edu/evespa/dadjokes/api/jokes', {
            method: 'post',
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              text: jokeText,
              contributor: author,
            })
          })
          const data = await response.json();
            // resets/clears the input fields after posting a new joke
          setJokeText("");
          setAuthor("");
          setIsPosting(false);
        } catch (error) {
          console.error("Error adding new joke:", error);
          setIsPosting(false);
        }
      };
    

  return (
    <View style={styles.container}>
    <Text style={styles.titleText}>Add a Joke (make sure it's funny)</Text>
     {/* input field for the joke text */}
    <TextInput
      style={styles.input}
      placeholder="Type your joke here"
      value={jokeText}
      onChangeText={setJokeText}
      multiline
    />
     {/* input field for the joke author */}
    <TextInput
      style={styles.input}
      placeholder="Type your name here"
      value={author}
      onChangeText={setAuthor}
      multiline
    />
    {/* button used to submit the new joke */}
    <TouchableOpacity style={styles.button} onPress={addJoke}>
        <Text style={styles.buttonText}>{isPosting ? 'Adding...' : 'Add Joke'}</Text>
    </TouchableOpacity>
  </View>
  );
}