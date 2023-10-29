import React from 'react';
import { Box, Flex, Text } from '@chakra-ui/react';

function Boxes({ result1, result2, result3 }) {
    return (
        <Flex
            direction="row"
            w="100%" // Set the width to 100% to make it fill the page horizontally
            // h="60vh" // Set the height of the container to 60vh for the entire viewport height
        //   bg="teal.1000"
        >
            <Box
                flex="1" // Let this box fill the available vertical space (bottom half)
                border="3px solid #ADD8E6" // Add a thin white border
                mx={2}
            >
                {/* {result1} */}
                <iframe 
                    width="100%" 
                    height="315" 
                    src={result1[0]}
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    allowfullscreen>
                </iframe>
                <Text>
                    {`distance: ${result1[3].toFixed(3)}`}
                </Text>
                <Text>
                    {`${result1[1]}-${result1[2]}`}
                </Text>
                <Text>
                    {result1[4]}
                </Text>
            </Box>
            <Box
                flex="1" // Each box within the flex container will fill the horizontal space evenly
                border="3px solid #ADD8E6" // Add a thin white border
                mx={2}
            >
                <iframe 
                    width="100%" 
                    height="315" 
                    src={result2[0]}
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    allowfullscreen>
                </iframe>
                <Text>
                {`distance: ${result2[3].toFixed(3)}`}

                </Text>
                <Text>
                {`${result2[1]}-${result2[2]}`}
                </Text>
                <Text>
                {result2[4]}

                </Text>
            </Box>
            <Box
                flex="1" // Each box within the flex container will fill the horizontal space evenly
                border="3px solid #ADD8E6" // Add a thin white border
                mx={2}
            >
                <iframe 
                    width="100%" 
                    height="315" 
                    src={result3[0]}
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    allowfullscreen>
                </iframe>
                <Text>
                {`distance: ${result3[3].toFixed(3)}`}

                </Text>
                <Text>
                {`${result3[1]}-${result3[2]}`}
                </Text>
                <Text>
                {result3[4]}

                </Text>
            </Box>
        </Flex>
    );
}

export default Boxes;