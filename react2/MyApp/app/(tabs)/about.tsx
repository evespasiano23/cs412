// File: about.tsx
// Author: Emily Vespasiano (evespa@bu.edu), 6/10/2026
// Description: The About screen tab which displays information about the author and an image.
import { Image, Text, View } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function AboutScreen() {

  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>About Me</Text>
      <Text style={styles.bodyText}>
        Hi! My name is Emily and I am currently a Comp. Sci student at BU. Photography is one of my passions.
        My favorite place to take photos in is New York City. I specifically love practicing street and 
        landscape photography!
      </Text>
      <Image
        source={require('../../assets/images/photo4.jpg')}
        style={styles.image}
      />
    </View>
  );
}