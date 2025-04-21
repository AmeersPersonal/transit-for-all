import { useState, useEffect } from 'react'
import { ScrollView, View, Text } from 'react-native';
import Clickable from '@/components/Clickable';
import { Double } from 'react-native/Libraries/Types/CodegenTypes';

const stations = ['59 St Columbus Circle', 'StationB', 'StationC', 'StationD'];

interface DataType {
  stop_id: string;
  stop_name: string;
  distance: Double;
  elevator: boolean;
  escalator: boolean;
}

const HomePage = ({ navigation }) => {
  const [data, setData] = useState<DataType[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const stationResponse = await fetch('http://10.0.2.2:5000/api/stations');

        if (!stationResponse.ok) {
          throw new Error(`HTTP error! status: ${stationResponse.status}`);
        }

        const stationJson: DataType[] = await stationResponse.json();
        setData(stationJson);

        
      } catch (e: any) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };
    fetchData();

  }, []);

  

  if (loading) {
    return <View><Text>Loading...</Text></View>;
  }

  if (error) {
    return <View><Text>Error: {error}</Text></View>;
  }

  return (
    <ScrollView>
      {data.map((station) => (
        <Clickable
          key={station.stop_id}
          title={station.stop_name}
          accessibilityDetails={[
          ]} 
          onPress={() => navigation.navigate('StationDetails', { station_id: station.stop_id, station_name: station.stop_name })}
        />
      ))}
    </ScrollView>
  );
};

export default HomePage;