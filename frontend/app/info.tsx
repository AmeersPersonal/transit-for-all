import { View, Text, ScrollView, StyleSheet, Image } from 'react-native';
import E from "../assets/images/icon.png";

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
  'w': require('../assets/images/w.png'),
  'z': require('../assets/images/z.png'),
};


const letters = ['a', 'b', 'c', 'd', '1']

const testData = [{
  
}]

const InfoPage = ({ route }) => {
  const { stationName } = route.params;
  return (
    <ScrollView>
      <View style={styles.Boxes}>
        <Text style={styles.Header}> {stationName}</Text>
        <View style={{flexDirection: 'row', flexWrap: 'wrap'}}>
          {letters.map((letter, index) => (
            <Image style={styles.Lines}
            key={index}
            source={images[letter]}
            />
          ))}
        </View>
      </View>
      <View style={styles.Boxes}>

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