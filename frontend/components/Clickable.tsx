import { TouchableOpacity, Text, View, StyleSheet} from 'react-native';

type ClickableProps = {
    title: string;
    accessibilityDetails: string[];
    onPress: () => void;
}

export default function Clickable({ title, accessibilityDetails, onPress }: ClickableProps) {
    return (
        <TouchableOpacity style={styles.button} onPress={onPress}>
          <View style={styles.row}>
            <Text style={styles.buttonText}>{title}</Text>
            <View style={styles.detailsContainer}>
              {accessibilityDetails.map((item, index) => (
                <Text style={styles.infoText} key={index}>{item}</Text>
              ))}
            </View>
          </View>
        </TouchableOpacity>
      );
    
}

// fetch('http://127.0.0.1:5000')
//   .then(response => response.text())       // get the raw text
//   .then(text => {
//     console.log('Received from Python:', text);  // just print it
//   })
//   .catch(err => console.error(err));


//fetch data from local host of the emulator
// interface Data {
//   message: string;
// }

// async function fetchData(): Promise<Data> {
//   const response = await fetch('http://10.0.2.2:5000');
//   const data: Data = await response.json();
//   return data;
// }

// fetchData().then(data => {
//   console.log(data.message); // Output: Hello from Python!
// });
const styles = StyleSheet.create({
    button: {
      margin: 4,
      backgroundColor: '#1E90FF',
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
    row: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      alignItems: 'center',
      width: '100%',
    },
    buttonText: {
      color: '#FFFFFF',
      fontSize: 24,
      fontWeight: '600',
    },
    detailsContainer: {
      flexDirection: 'column',
      gap: 8, // works if you're using React Native 0.71+
    },
    infoText: {
      color: '#FFFFFF',
      fontSize: 16,
      fontWeight: '600',
      marginLeft: 8,
    },
  });