import Clickable from '@/components/Clickable';

const FlatListBasics = () => {
  return (
    <>
      <Clickable title="StationA" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes', 'Info: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationB" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes', 'Info: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationC" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes', 'Info: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationD" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes', 'Info: Yes']} onPress={() => alert('Button pressed!')}/>
    </>

  );
};

export default FlatListBasics;