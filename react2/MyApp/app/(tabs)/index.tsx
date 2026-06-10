// File: index.tsx
// Author: Emily Vespasiano (evespa@bu.edu), 6/10/2026
// Description: The Index screen tab which displays information about photography.
import { Image, Text, View } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function IndexScreen() {

  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>
        Photography
      </Text>
      <Text style={styles.bodyText}>
        Photography is one of my favorite hobbies. I enjoy telling stories through a lense, specifically
        at places that I travel to. The photo below was taken of this couple in Aspen, Colorado last summer.
      </Text>
      <Image
        source={require('../../assets/images/colorado.jpg')}
        style={styles.image}
      />
    </View>
  );
}