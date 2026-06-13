// File: index.tsx
// Author: Emily Vespasiano (evespa@bu.edu), 6/13/2026
// Description: The Index screen tab which displays a random joke and picture.
import { Text, View, Image, ActivityIndicator, TouchableOpacity } from 'react-native';
import { styles } from '../../assets/my_styles';
import { useState, useEffect }  from 'react';

export default function IndexScreen() {

  // tracks the joke, picture, and loading state
  const [joke, setJoke] = useState(null);
  const [picture, setPicture] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  const fetchRandomJoke = async () => {
  // fetches a random joke from the API
    try {
      const response = await fetch("https://cs-webapps.bu.edu/evespa/dadjokes/api/random");
      const data = await response.json();
      setJoke(data);
    } catch (error) {
      console.error("Error fetching joke:", error);
    }
  };

  const fetchRandomPicture = async () => {
   // fetches a random picture from the API
    try {
      const response = await fetch("https://cs-webapps.bu.edu/evespa/dadjokes/api/random_picture");
      const data = await response.json();
      setPicture(data);
      setIsLoading(false);
    } catch (error) {
      console.error("Error fetching picture:", error);
      setIsLoading(false);
    }
  };

  // when the screen loads this fetches a random joke and picture 
  useEffect(() => {
    fetchRandomJoke();
    fetchRandomPicture();
  }, [])

  // shows the loading symbol on screen while fetching data
  if (isLoading) {
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" color="#0000ff" />
        <Text>Loading...</Text>
      </View>
    )
  }

  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>Random Dad Joke 🤣</Text>
      {/* displays the random joke text and contributor */}
      <Text style={styles.bodyText}>{joke.text}</Text>
      <Text style={styles.contributorText}>— {joke.contributor}</Text>
      {/* displays the random picture */}
      <Image
        source={{ uri: picture.image_url }}
        style={styles.image}
      />
      {/* button for user to get a new random joke and picture */}
      <TouchableOpacity style={styles.button} onPress={() => {
        fetchRandomJoke();
        fetchRandomPicture();
      }}>
        <Text style={styles.buttonText}>New Joke (get ready to laugh)🤣</Text>
      </TouchableOpacity>
    </View>
  )
}