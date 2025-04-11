import { View, Text, ScrollView, StyleSheet } from 'react-native';
// import { ScrollView } from 'react-native-reanimated/lib/typescript/Animated';

const InfoPage = ({ route }) => {
  const { stationName } = route.params;
  return (
    <ScrollView>
      <View style={styles.Boxes}>
        <Text style={styles.Header}> {stationName}</Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
    Header: {
      fontSize: 32,
      color: '#000000',
      fontWeight: '600',
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
  });

export default InfoPage;