// File: jokes_list.tsx
// Author: Emily Vespasiano (evespa@bu.edu), 6/13/2026
// Description: The Jokes List screen tab which displays all dad jokes.
import { Text, View, FlatList, ActivityIndicator } from 'react-native';
import { styles } from '../../assets/my_styles';
import { useState, useEffect } from 'react';

export default function JokeListScreen() {

// tracks the jokes, loading state, and refresh state
const [jokeList, setJokeList] = useState([]);
const [isLoading, setIsLoading] = useState(true);
const [refreshing, setRefreshing] = useState(false);

const fetchJokes = async () => {
// fetches all jokes from the API
  try {
    const response = await fetch("https://cs-webapps.bu.edu/evespa/dadjokes/api/jokes");
    const data = await response.json();
    setJokeList(data.results);
    setIsLoading(false);
  } catch (error) {
    console.error("Error fetching jokes:", error);
    setIsLoading(false);
  }
};

// displays and works the pull to refresh function to reload all jokes list
const handleRefresh = () => {
  setRefreshing(true);
  fetchJokes();
  setRefreshing(false);
};

  // when the screen loads this fetches the list of jokes
useEffect(() => {
  fetchJokes();
}, [])

  // shows the loading symbol on screen while fetching data
if (isLoading) {
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" color="#0000ff" />
        <Text>Loading...</Text>
      </View>
    );
  }


  return (
    <View style={styles.container}>
          <Text style={styles.titleText}>All Dad Jokes 😅</Text>
           {/* text for pull to refresh clarification */}
          <Text style={{fontSize: 12, color: 'gray', marginBottom: 10, textAlign: 'center'}}>Pull down to refresh</Text>
          {/* list of all dad jokes */}
          <FlatList
            data={jokeList}
            renderItem={({ item }) => (
              <View style={styles.card}>
                <Text style={styles.bodyText}>{item.text}</Text>
                <Text style={styles.contributorText}>— {item.contributor}</Text>
              </View>
            )}
            ItemSeparatorComponent={() => (
              <View style={{ height: 16 }} />
            )}
            refreshing={refreshing}
            onRefresh={handleRefresh}
          />
        </View>
  )
}