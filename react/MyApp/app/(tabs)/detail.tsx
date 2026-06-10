// File: detail.tsx
// Author: Emily Vespasiano (evespa@bu.edu), 6/10/2026
// Description: The Detail screen tab which displays information about various images.
import { Image, Text, View, ScrollView } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function DetailScreen() {

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.titleText}>City Photography</Text>
      <Text style={styles.bodyText}>This photo was taken of a saxophonist performing at Washington Square Park, 
      which happens to be my favorite place in New York City.</Text>
      <Image
        source={{uri: 'http://cs-people.bu.edu/evespa/images/photo1.jpg' }}
        style={styles.image}
      />
      <Text style={styles.bodyText}>I took this photo on my birthday last July in New York City of
      the New Yorker building. It's one of my favorite photos.</Text>
      <Image
        source={{uri: 'http://cs-people.bu.edu/evespa/images/photo2.jpg' }}
        style={styles.image}
      />
      <Text style={styles.bodyText}>I took this photo in Fenway on Jersey Street 
      while I was crossing the street!</Text>
      <Image
        source={{uri: 'http://cs-people.bu.edu/evespa/images/photo3.jpg' }}
        style={styles.image}
      />
    </ScrollView>
  );
}