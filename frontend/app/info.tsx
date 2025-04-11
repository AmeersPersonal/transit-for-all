import { View, Text, ScrollView, StyleSheet, Image } from 'react-native';
import E from "../assets/images/icon.png";
import { useEffect, useState } from 'react';

// import { ScrollView } from 'react-native-reanimated/lib/typescript/Animated';
const images = {
  '1': require('../assets/images/1.png'),
  '2': require('../assets/images/2.png'),
  '3': require('../assets/images/3.png'),
  '4': require('../assets/images/4.png'),
  '5': require('../assets/images/5.png'),
  '6': require('../assets/images/6.png'),
  '6d': require('../assets/images/6d.png'),
  '7': require('../assets/images/7.png'),
  '7d': require('../assets/images/7d.png'),
  'a': require('../assets/images/a.png'),
  'b': require('../assets/images/b.png'),
  'c': require('../assets/images/c.png'),
  'd': require('../assets/images/d.png'),
  'e': require('../assets/images/e.png'),
  'f': require('../assets/images/f.png'),
  'fd': require('../assets/images/fd.png'),
  'g': require('../assets/images/g.png'),
  'j': require('../assets/images/j.png'),
  'l': require('../assets/images/l.png'),
  'm': require('../assets/images/m.png'),
  'n': require('../assets/images/n.png'),
  'q': require('../assets/images/q.png'),
  'r': require('../assets/images/r.png'),
  's': require('../assets/images/s.png'),
  'sir': require('../assets/images/sir.png'),
  'w': require('../assets/images/w.png'),
  'z': require('../assets/images/z.png'),
};

interface OutageData {
  "type":string,
  "reason":string,
  "outage_date":string,
  "return_serice":string,
  "service_area":string,
}

const InfoPage = ({ route }) => {
    const { station_id, station_name } = route.params;


    const [lineData, setLineData] = useState<string[]>([]);
    const [outageData, setOutageData] = useState<OutageData[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const lineResponse = await fetch(`http://10.0.2.2:5000/api/lines/A24N`);
  
          if (!lineResponse.ok) {
            throw new Error(`HTTP error! status: ${lineResponse.status}`);
          }
  
          const lineJson: string[] = await lineResponse.json();
          setLineData(lineJson);

          const outageResponse = await fetch(`http://10.0.2.2:5000/api/outages/${station_name}`);
  
          if (!outageResponse.ok) {
            throw new Error(`HTTP error! status: ${outageResponse.status}`);
          }
  
          const outageJson: OutageData[] = await outageResponse.json();
          setOutageData(outageJson);
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
      <View style={styles.Boxes}>
        <Text style={styles.Header}> {station_name}</Text>
        <View style={{flexDirection: 'row', flexWrap: 'wrap'}}>
          {lineData.map((letter, index) => (
            <Image style={styles.Lines}
            key={index}
            source={images[letter.toLowerCase()]}
            />
          ))}
        </View>
      </View>
      {outageData.length > 0} ? 
      {outageData.map((info, index) => (
        <View style={styles.Boxes}>
          <Text style={styles.InfoHeader}>Outage</Text>
          <Text style={styles.Info}>Type: {info.type}</Text>
          <Text style={styles.Info}>Date Outage Started: {info.outage_date}</Text>
          <Text style={styles.Info}>Estimated Outage Fix: {info.return_serice}</Text>
          <Text style={styles.Info}>Outage Reason: {info.reason}</Text>
          <Text style={styles.Info}>Outage Area Affected: {info.service_area}</Text>
        </View>
      ))}
      :
      <View style={styles.Boxes}>
          <Text style={styles.InfoHeader}>No Current Outages</Text>
        </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
    Header: {
      fontSize: 32,
      color: '#000000',
      fontWeight: '600',
      marginBottom: 12
    },
    InfoHeader: {
      fontSize: 32,
      color: '#000000',
      fontWeight: '600',
      marginBottom: 12,
    },
    Info: {
      fontSize: 20,
      color: '#000000',
      fontWeight: '600',
      marginBottom: 6,
      flexShrink: 1
    },
    Boxes: {
      margin: 4,
      backgroundColor: '#FFFFFF',
      paddingVertical: 12,
      paddingHorizontal: 24,
      borderRadius: 8,
      alignItems: 'stretch', // allow flex row to stretch inside
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.3,
      shadowRadius: 4,
      elevation: 3,
    },
    Lines: {
      width: 50, 
      height: 50, 
      marginRight: 8,
      marginBottom: 8,
    }
  });

export default InfoPage;