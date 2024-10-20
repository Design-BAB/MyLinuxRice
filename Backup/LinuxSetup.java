import java.nio.file.*;

public class LinuxSetup {
    public static void main(String[] args) {
      String title1 = " |  \/  (_) |        ( )     | |    (_)                   / ____|    | |";  
      System.out.println(title1);
        
        System.out.println("We are now going to install catimg.");
        System.out.println("The goal is to get Miku to be display in terminal.");
        try {
            String command = "sudo apt install catimg";  // Replace with your package name
            Process process = Runtime.getRuntime().exec(command);

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            int exitCode = process.waitFor();
            System.out.println("Exited with code: " + exitCode);
        } catch (Exception e) {
            e.printStackTrace();
        }
    
        System.out.println("Hello! so the first thing we will do is to replace the bashrc file.");
        System.out.println("This file tells the terminal what to do everytime you open it up.");
        Path source = Paths.get("bashrc");
        Path target = Paths.get("~/.bashrc");

        try {
            Files.move(source, target, StandardCopyOption.REPLACE_EXISTING);
            System.out.println("File replaced successfully.");
        } catch (IOException e) {
            e.printStackTrace();

        }
    }
}

