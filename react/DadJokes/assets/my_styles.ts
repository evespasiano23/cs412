// File: my_styles.ts
// Author: Emily Vespasiano (evespa@bu.edu), 6/13/2026
// Description: StyleSheet for all three tabs in DadJokes.
import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
    // main style for all three tab screens
    container: {
        flex: 1, 
        backgroundColor: '#D6EEFF', 
        padding: 60,
    },
    // title text style for headers
    titleText: {
        fontSize: 30, 
        fontWeight: 'bold',
        marginBottom: 4,
        textAlign: 'center',
        color: '#9b59b6',
        letterSpacing: 2,
    },
    // body text style for jokes
    bodyText: {
        fontSize: 16, 
        marginBottom: 24,
        textAlign: 'center',
        color: '#9b59b6',
    },
    // image style for pictures
    image: {
        width: '100%', 
        height: 220, 
        resizeMode: 'cover',
        borderWidth: 3,
        borderColor: '#9b59b6',
        borderRadius: 12,
    },
    // button style for user touchable buttons
    button: {
        backgroundColor: '#2ecc71',
        padding: 12,
        borderRadius: 8,
        alignItems: 'center' as 'center',
        marginTop: 10,
    },
    // text style for the buttons
    buttonText: {
        color: 'white',
        fontSize: 16,
        fontWeight: 'bold' as 'bold',
    },
    // card style for each dad joke in the joke list
    card: {
        backgroundColor: 'white',
        padding: 16,
        borderRadius: 12,
        borderLeftWidth: 5,
        borderLeftColor: '#9b59b6',
        marginBottom: 10,
      },
    // style for text input fields
    input: {
        height: 100,
        borderColor: '#2ecc71',
        borderWidth: 2,
        marginBottom: 16,
        padding: 8,
        borderRadius: 8,
        backgroundColor: 'white',
      },
    // text style for joke creator
    contributorText: {
        fontSize: 16,
        marginBottom: 24,
        textAlign: 'center',
        color: '#9b59b6',
        fontWeight: 'bold',
      },
});