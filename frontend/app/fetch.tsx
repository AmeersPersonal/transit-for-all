import React, { useEffect, useState } from 'react';
import { View, Text } from 'react-native';
import Clickable from '@/components/Clickable';

interface Station {
  name: string;
  elevator: boolean;
  escalator: boolean;
}

export default function FlatListBasics() {
  // 1) We keep an array of Station objects in state
  const [stations, setStations] = useState<Station[]>([]);

  // 2) Use useEffect to fetch data once the component loads
  useEffect(() => {
    // For Android Emulator:
   
    // For iOS simulator or web:
    fetch('http://10.0.2.2:5000/api/stations')
      .then((res) => res.json())
      .then((data: Station[]) => {
        setStations(data);  // store stations in our state
      })
      .catch((err) => console.error('Error fetching:', err));
  }, []);

  // 3) Map over the fetched stations array to create Clickable components
  return (
    <View>
      {stations.map((station, index) => (
        <Clickable
          key={index}
          title={station.name}
          accessibilityDetails={[
            `Elevators: ${station.elevator ? 'Yes' : 'No'}`,
            `Escalators: ${station.escalator ? 'Yes' : 'No'}`,
          ]}
          onPress={() => alert(`Clicked ${station.name}`)}
        />
      ))}
    </View>
  );
}
