// File: _layout.tsx
// Author: Emily Vespasiano (evespa@bu.edu), 6/13/2026
// Description: Contains the tab navigation layout for the DadJokes application.
import { SymbolView } from 'expo-symbols';
import { Link, Tabs } from 'expo-router';

import Colors from '@/constants/Colors';
import { useColorScheme } from '@/components/useColorScheme';
import { useClientOnlyValue } from '@/components/useClientOnlyValue';

export default function TabLayout() {
  // gets the current color scheme for styling
  const colorScheme = useColorScheme();

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors[colorScheme].tint,
        headerShown: useClientOnlyValue(false, true),
      }}>
      {/* tab for random joke and picture */}
      <Tabs.Screen
        name="index"
        options={{
          title: 'Random',
          tabBarIcon: ({ color }) => (
            <SymbolView
              name={{
                ios: 'die.face.5',
                android: 'casino',
                web: 'casino',
              }}
              tintColor={color}
              size={28}
            />
          ),
        }}
      />
      {/* tab for jokes list */}
      <Tabs.Screen
        name="jokes_list"
        options={{
          title: 'Jokes',
          tabBarIcon: ({ color }) => (
            <SymbolView
              name={{
                ios: 'face.smiling',
                android: 'mood',
                web: 'mood',
              }}
              tintColor={color}
              size={28}
            />
          ),
        }}
      />
      {/* tab for adding/creating a new joke */}
      <Tabs.Screen
        name="add_joke"
        options={{
          title: 'Add Joke',
          tabBarIcon: ({ color }) => (
            <SymbolView
              name={{
                ios: 'plus.circle',
                android: 'add',
                web: 'add',
              }}
              tintColor={color}
              size={28}
            />
          ),
        }}
      />
    </Tabs>
  );
}