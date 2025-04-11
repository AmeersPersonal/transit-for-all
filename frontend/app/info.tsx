import { Text, StyleSheet } from 'react-native';

const infoPage = () => {
  return (
    <Text> Hello World!</Text>
  );
};

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
      fontSize: 32,
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

export default infoPage;