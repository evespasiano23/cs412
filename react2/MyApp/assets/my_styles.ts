// File: my_styles.ts
// Author: Emily Vespasiano (evespa@bu.edu), 6/10/2026
// Description: StyleSheet for all three tabs in MyApp.
import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
    container: {
        flex: 1, backgroundColor: '#E6E6FA', padding: 60,},
    titleText: {
        fontSize: 30, fontWeight: 'bold', marginBottom: 16,},
    bodyText: {
        fontSize: 16, marginBottom: 24,},
    image: {
        width: '100%', height: 220, resizeMode: 'contain',},
});