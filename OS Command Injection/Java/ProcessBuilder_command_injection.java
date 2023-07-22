import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class ProcessBuilder_command_injection {

	public static void main(String[] args) throws IOException {
    String input = args[0];

    ProcessBuilder builder = new ProcessBuilder();
    builder.command("/bin/bash", "-c", "touch /tmp/" + input);
    Process process = builder.start();
	}

}