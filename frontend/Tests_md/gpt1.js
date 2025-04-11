
import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';

export default function App() {
  const [stations, setStations] = useState([]);

  useEffect(() => {
    fetch('http://10.0.2.2:5000/api/stations') // Use your IP if testing on real phone
      .then(response => response.json())
      .then(data => setStations(data))
      .catch(error => console.error('Error fetching stations:', error));
  }, []);

  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <Text style={styles.name}>{item.name}</Text>
      <Text>Elevator: {item.elevator ? '✅' : '❌'}</Text>
      <Text>Escalator: {item.escalator ? '✅' : '❌'}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Accessible Subway Stations</Text>
      <FlatList
        data={stations}
        renderItem={renderItem}
        keyExtractor={(item, index) => index.toString()}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, paddingTop: 40, paddingHorizontal: 16 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  card: { padding: 16, borderBottomWidth: 1, borderColor: '#ddd' },
  name: { fontSize: 18, fontWeight: 'bold' },
});
